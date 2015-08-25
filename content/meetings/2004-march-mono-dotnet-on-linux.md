Title: March 2004 meeting minutes
Author: Joe
Date: 2004-03-13 10:37
Category: meetings
Tags: meeting-minutes, meetings-2005, mono, .NET

**Topic**: Mono.NET, DotNET on GNU/Linux

**Speaker**: Mr. Kaushik Srenevasan

**Venue**: Z0 Lecture Hall, CSE Department, Thiagarajar College of Engineering, Madurai - 625015

**Topics discussed**:

In today's meet we spoke about,

1. Understanding what .NET is
2. Discuss history behind the Mono project
3. Demonstrate some Mono components
4. Other open source alternatives

**Introduction**:

.NET a platform for building and running the next generation of applications and XML Web services. It provides a highly productive, standard based, enterprise-ready, Multilanguage environment that simplifies application development, enables developers to leverage their existing skill set, facilitates integration with existing software, and eases the challenges of deploying and operating Internet-scale applications.

The Framework consists of two main parts: (1) the common language runtime and (2) a unified, hierarchical class library that includes a revolutionary advance to Active Server Pages (ASP.NET) and a loosely-coupled data access subsystem (ADO.NET).

**Basics**:

**Platform**:

A development environment provides a set of programmatic services, exposed through some API to developers using one or more languages.

The Framework, as any other development environment, can be broken down into three fundamental areas: the runtime the platform offers, the libraries it defines, and the languages we can use to target it.

**Runtime**:

A runtime is a piece of code, written by the platform vendor that provides our code with a set of services. These services could be anything - from checking security, to implementing a file system, to providing access to some piece of hardware.

Almost every program takes advantage of some sort of runtime. Very few programmers start a project by writing their own file system or database engine. Rather, they make use of already-written pieces of software, like Linux or mySQL. In the case of Linux, the runtime is the OS kernel, and it provides services like thread management. In the case of mySQL, the runtime is the database engine, and the services include things like a SQL engine and transactions.

The Framework provides these services using a layered architecture (as shown below). In some cases application code uses the CLR directly and in others indirectly.

**Libraries**:

The Framework SDK provides an API to interact with the runtime. This API takes the form of a set of classes. Collectively, they are referred to the Base Class Libraries, or BCL. Through the classes in the BCL, we can interact with the runtime, influencing the way that the runtime's services are provided to us.

The BCL classes also provide a large amount of useful utilities. These include things like a new database access library (ADO.NET), ASP.NET, and an XML parser with support for the latest XML specifications. There are thousands of classes in the BCL.

Languages: In order to take advantage of a set of libraries and the runtime we need to use some programming language with a compiler that is runtime-aware. There are currently two languages that Mono supports C# and Mono Basic (VB on Mono)

**Standards Based**:

The Framework provides explicit support for standards, making extensive use of technologies like XML and SOAP.

In addition to helping write applications that conform to accepted standards - meaning our applications have a better chance of being able to interoperate with other applications over the Internet - the CLR itself is an implementation of a standard. Microsoft has submitted the CLI - the Common Language Infrastructure - to ECMA. The CLI is the specification that describes the CLR. It can be found at http://www.ecma.ch.

**What is in Mono?**

* Common Language Infrastructure (CLI) virtual machine
* Class loader
* Just-in-time compiler
* Garbage collecting runtime
* Class library that can work with any language which works on the CLR.
* .NET compatible class libraries
* Mono-provided class libraries
* Compiler for the C# language (**Note**: Other compilers that target the CLR in the future Mono Platform support Just In Time (JIT) compiler for x86 systems;)
    * Linux
    * FreeBSD
    * Windows (XP/NT core)
    * PowerPC
    * Interpreter (slower)
    * s390
    * SPARC
    * PowerPC
 * Mono Assemblies
 * Core
 * mscorlib
 * System, System.XML, System.Security
 * WinForms
 * Windows.Forms
 * GDI+
 * System.Drawing
 * ADO.NET
 * System.Data
 * Various other database providers.
 * ASP.NET
 * System.Web, System.Web.Service
 * Microsoft.VisualBasic
 * System.Runtime.Serialization.Formatters.Soap

**Mono Development Tools**:

**Compilers**

mcs : Mono C# compiler

mbas : Mono Basic (supserset of VB.NET) compiler

mono : Mono Just-in-Time and Ahead-of-Time code generator

mint - Mono interpreter

wsdl : WSDL utility. Generates web service client proxy and service from WSDL document.

Other command line tools and utilities

**How do I get Mono?**

Mono website - [http://www.go-mono.com/](http://www.go-mono.com/)

Available downloads:

Source code
Linux x86
Redhat 9
Fedora Core 1
SuSE
Debian
Windows
(Current release is 0.30.1)

--
MOM contributed by Kaushik Srenevasan
