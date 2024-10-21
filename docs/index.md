# Техническая документация hex64 Diagnostic
hex64 Diagnostic позволяет анализировать, мониторить и тестировать ваш ПК. hex64 Diagnostic имеет CLI-интерфейс, а также имеет возможность использования как библиотеку.

```
---------------------------------------------------------------------------------
   __ _______  __  ____ ____         hex64 Diagnostic v0.15.18
  / // / __/ |/_/ / __// / /         PC Monitoring, Analysing, Diagnostic Toolkit
 / _  / _/_>  <  / _ \/_  _/         developed by alxvdev
/_//_/___/_/|_|  \___/ /_/           https://github.com/alxvdev/hex64
---------------------------------------------------------------------------------
```

## Содержание
Все статьи, связанные с технической документацией проекта.

 > Документация пока не доступна и находится в процессе написания. Среди доступных есть только "Архитектура проекта".

 + [Архитектура проекта](./project_architecture.md)
 - [Дополнительные утилиты](./other_utils.md)
 - [Сбор информации о процессоре](./infrastructure_cpusensor.md)
 - [Сбор информации об оперативной памяти](./infrastructure_ramsensor.md)
 - [Сбор информации о температурах](./infrastructure_tempsensor.md)
 - [Сбор информации о диске и его разделах](./infrastructure_disksensor.md)
 - [Однопроцессорный бенчмарк процессора](./infrastructure_cpu_singlecore_benchmark.md)
 - [Многопроцессорный бенчмарк процессора](./infrastructure_cpu_multicore_benchmark.md)
 - [Хранение и использование информации от сенсоров](./infrastructure_hardwarerepository.md)
 - [Хранение и использование информации из бенчмарок](./infrastructure_benchmarkrepository.md)

## Дополнительный материал
Статьи, написанные авторами про наш проект.

 + [Пишем свою программу для бенчмаркинга и мониторинга ресурсов на Python](./article.md)

## История версий

+ 0.1.0 - base architecture
+ 0.1.1 - base utils
+ 0.1.2 - cpu sensor
+ 0.2.2 - ram sensor
+ 0.2.3 - benchmark module architecture
+ 0.3.3 - temp sensor
+ 0.4.3 - disk sensor
+ 0.5.3 - cpu single/multi benchmark
+ 0.6.3 - create hardware repository
+ 0.6.4 - fix bugs, fix docstrings
+ 0.7.4 - create benchmark repository
+ 0.7.5 - fixing bugs in benchmarks, improve multi benchmark
+ 0.7.6 - improve hardware repository and fix bugs
+ 0.7.7 - replace settings by constants in config module (and add basic constants)
+ 0.7.8 - improve utils module
+ 0.7.9 - improve docs
+ 0.7.10 - improve cpu sensor, fix data convertor
+ 0.8.10 - add network sensor
+ 0.8.11 - improve disk sensor
+ 0.8.12 - fix docstrings, fix small bugs
+ 0.9.12 - add plots_generator with plots module
+ 0.9.13 - add disk plot generator in plots module
+ 0.9.14 - improve docs and docstrings
+ 0.10.14 - create domain entities zone (hardware)
+ 0.10.15 - create GUI App colorscheme
+ 0.10.16 - create base gui ui template
+ 0.10.17 - improve gui (cpu info)
+ 0.11.17 - improve gui (cpu info tab done)
+ 0.12.17 - improve gui (ram info tab done)
+ 0.13.17 - improve gui (disk info tab done)
+ 0.14.17 - improve gui (temp info tab done)
+ 0.15.17 - improve gui (network info tab done)
+ 0.15.18 - small bugfix and small changes in gui (information tab is done)