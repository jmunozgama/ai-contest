# Sandboxing #



## What is Sandboxing? ##

In our programming contests, contestants submit their code using a web interface. The code is then compiled and run by our servers. This presents several security issues. A malicious or careless person may submit code that attempts to:
  * delete files
  * make network connections to outside servers
  * spawn an extraordinary number of threads (forkbomb)
  * interfere with other submissions
  * connect to or wreck the contest's database
  * any number of other nasty things

It is for this reason that we need to run untrusted code inside a "sandbox", or "padded cell". The sandbox prevents untrusted programs from doing bad things. There are several different ways to sandbox untrusted code.

## Ptrace ##

Ptrace can be used to sandbox untrusted code by intercepting potentially harmful system calls. However, this approach has been judged to be unsuitable because:
  * it is difficult to follow the execution of a program if it forks a new thread
  * systrace basically does the same thing anyways, except it's easier to use

## Systrace ##

Systrace is a program that invokes an untrusted program, and uses ptrace to intercept syscalls made by the untrusted program. Whenever a syscall is intercepted, Systrace uses policies that are defined in a text file to decide whether or not to allow the syscall. This allows us to have fairly fine-grained control over what programs are and are not allowed to do.

Nevertheless, there is a fairly large disadvantage to using Systrace. It can be slow. Every time a syscall is intercepted by the kernel, the system has to wait until the next time that the Systrace process is scheduled before it can decide whether to allow or deny the syscall. Then the system has to wait until the next time that the untrusted program is scheduled to run before the result of the syscall can be returned. This process of alternation between the untrusted program and Systrace can really slow things down, especially for interpreted languages.

The slowness is especially pronounced when running Java programs. The JVM uses a large number of threads, even to execute relatively simple programs. Because of this, there are long delays between the time when a syscall is issued by a JVM thread and the time when the reply is received and acted upon. In particular, Java programs have trouble staying under the per-move time limit, because by the time they're able to figure out how much time has elapsed, they have often already run over the time limit. This is very frustrating for Java users, because there's nothing they can do to fix it.

The performance for languages besides Java seems to be satisfactory. If we can figure out some other way to sandbox Java and use Systrace for everything else, that should do the trick. Therefore we judge that Systrace-based sandboxing is a viable option.

Systrace was used with great success to secure the Google AI Challenge in Winter 2010. The only hickup was that it was close to impossible to create a competitive entry in Java. All other languages seemed to be okay.

## SMACK ##

SMACK stands for Simplified Mandatory Access Control Kernel. It works similarly to Systrace and ptrace, by intercepting syscalls and deciding whether to allow or deny them based on a policy.

The advantage of SMACK is that it would likely be much faster than Systrace. SMACK makes the decision about whether to allow or deny a syscall in the kernel side of the process being monitored. Therefore, the issue of alternation between Systrace and the untrusted process is eliminated. We expect that using SMACK would eliminate the Java problem.

There are several disadvantages to using SMACK:
  * SMACK seems to be more complicated to setup and configure than Systrace
  * SMACK is not yet integrated into the kernels of standard Ubuntu or Debian, and may never be. In order to use it, you need to use a specially-compiled kernel.

The disadvantages are manageable for the contest staff, it seems. However, the disadvantages could discourage independent developers from pulling down the code and tinkering with it. Ideally, we would have a contest system that can be setup and launched on a typical Ubuntu laptop within a few minutes. If somebody has to recompile their kernel in order to launch a contest instance, that will be a big barrier to entry for the project. This limitation can be overcome by providing a default sandbox which performs no security beyond per-move time limit enforcement, with the option to turn on SMACK-based sandboxing if you really want to.