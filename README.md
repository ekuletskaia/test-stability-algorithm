# test-stability-algorithm

Демонстрационные материалы к статье  
**«Алгоритм оптимизации автоматизированного тестирования мобильных приложений: повышение стабильности и оценка эффективности по ключевым метрикам»**  
(Е. Кулецкая, 2025).

---

## 🇷🇺 Описание

Репозиторий содержит демонстрационные материалы, сопровождающие статью.  
Включает примеры кода на Python, шаблоны конфигурации Appium, демонстрационные данные и результаты экспериментов.  
Все материалы обезличены и не содержат данных конкретных проектов.

### Структура
- `/env/` — настройки среды (capabilities, зависимости, конфигурация Appium)
- `/code/` — примеры кода (ожидания, прокрутка, retry, шаблон теста)
- `/data/` — примеры метрик до/после оптимизации и по спринтам
- `/results/` — визуальные материалы (блок-схема алгоритма, графики, таблицы)

### Воспроизводимость
1. Установить зависимости:  
   `pip install -r env/requirements.txt`
2. Настроить Appium-среду в соответствии с `env/appium_config.md`.
3. Использовать шаблоны из `/code/` для реализации шагов алгоритма (листинги 1–3).
4. Сравнить результаты с демонстрационными метриками из `/data/`.

### Лицензия
Материалы предоставлены только для академического и некоммерческого использования.

---

#### Цитирование
Репозиторий сопровождает статью:  
*(ссылка и DOI будут добавлены после публикации).*

---

# Algorithm for Optimizing Automated Test Stability for Mobile Applications

## Overview

This repository contains supplementary materials for the article  
**“Algorithm for Optimizing Automated Test Stability for Mobile Applications”**  
by *L. Kuletsky (2025)*.

It includes example Python code fragments, Appium environment configuration templates,  
and demonstration datasets used to reproduce the stability optimization experiment.

No proprietary or project-specific code is included —  
all examples are generic and serve only to illustrate the proposed algorithm and metrics calculation.

## Structure
- `/env/` — environment configuration (capabilities, dependencies, Appium setup)
- `/code/` — example code (waits, scroll, retry, test template)
- `/data/` — example metrics before/after optimization and sprint data
- `/results/` — illustrative materials (block diagram, graphs, tables)

## Reproducibility
To reproduce the experiment steps:
1. Install dependencies:  
   `pip install -r env/requirements.txt`
2. Configure Appium as described in `env/appium_config.md`.
3. Use code templates from `/code/` to implement the described algorithm (Listings 1–3).
4. Compare your results with demo datasets in `/data/`.

## License
The repository is provided for academic and non-commercial use only.

---

### Citation / Цитирование
This repository accompanies the article:  
*(publication link and DOI will be added after journal release).*
