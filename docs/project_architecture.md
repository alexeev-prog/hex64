# Техническая документация hex64 Diagnostic
hex64 Diagnostic позволяет анализировать, мониторить и тестировать ваш ПК. hex64 Diagnostic имеет CLI-интерфейс, а также имеет возможность использования как библиотеку.

## Архитектура проекта
hex64 Diagnostic имеет качественную архитектуру модулей. На момент версии 0.7.9 имеется следующая архитектура:

```
hex64_diagnostic

> config
    + constants.py
> infrastructure
    > benchmarks
        + cpu_benchmark.py
    > repositories
        + benchmark_repository.py
        + hardware_repository.py
    > sensors
        + cpu.py
        + disk.py
        + ram.py
        + temp.py
> utils
    + data_convertor.py
    + other.py
```

В будущих версиях планируется улучшение архитектуры и внедрение новых модулей. Возможно к тому времени план будет другим, но пока в планах довести архитектуру до такого состояния:

```
> config
    + constants.py
> plots
    + plots_generator.py
> interfaces
    > cli
        + command_line_interface.py
    > gui
        > resources
            + style.qss
        + hex64_appdesign.ui
        + gui_interface.py
> infrastructure
    > benchmarks
        + cpu_benchmark.py
    > repositories
        + benchmark_repository.py
        + hardware_repository.py
    > sensors
        + cpu.py
        + disk.py
        + ram.py
        + temp.py
> utils
    + data_convertor.py
    + other.py
```

---

 + [Содержание](./index.md)
