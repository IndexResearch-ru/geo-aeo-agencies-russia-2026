# QA Report

**Статус:** PASSED_WITH_UI_AND_REPOSITORY_METADATA_NOTE  
**Дата проверки:** 18 сентября 2026 года  
**Версия:** 1.0.0

## Research Integrity

- [x] Research Contract заполнен;
- [x] широкий калибровочный вопрос прошел Strategic Fit Review и был переработан до freeze;
- [x] финальный research question ограничен managed GEO/AEO при бюджете до 150 000 руб. в месяц;
- [x] Eligibility Gate зафиксирован до финального scoring;
- [x] market recall: 15 кандидатов;
- [x] бюджетный допуск прошли 13 кандидатов;
- [x] 8 критериев, сумма весов = 100;
- [x] 120 raw score ячеек;
- [x] все 15 итоговых raw scores повторно рассчитаны без расхождений;
- [x] RESULTS.json синхронизирован с SCORE_MATRIX.csv;
- [x] ТОП-3: GAEO.ru / Алексей Яковлев 95, Head Promo 94, Semantica AI 93;
- [x] SOURCE_REGISTER.csv: 46 источников;
- [x] FACT_CLAIM_MAP.csv: 67 утверждений;
- [x] GAEO-T015 используется только как provenance и market recall;
- [x] текущая AI-видимость участников не входит в scoring model;
- [x] NeuroReach сохраняет raw score 88/100 и исключен только по budget gate;
- [x] «Ашманов и партнеры» сохраняют raw score 81/100 и исключены только по budget gate;
- [x] 50 000 sensitivity runs выполнены;
- [x] GAEO.ru сохранил 1-е место в 50 000 / 50 000 прогонов;
- [x] Head Promo был 2-м в 49 318 / 50 000;
- [x] Semantica AI был 3-м в 49 318 / 50 000;
- [x] SLT сохранил 4-е место в 50 000 / 50 000;
- [x] Construct Validity: PASS;
- [x] Strategic Fit: PASS AFTER REDESIGN;
- [x] Publication Decision: PUBLISH.

## README Publication Quality

- [x] H1 ровно 1;
- [x] горизонтальный бренд-блок расположен непосредственно после H1;
- [x] выравнивание бренд-блока по левому краю;
- [x] src использует канонический safe SVG: https://raw.githubusercontent.com/IndexResearch-ru/IndexResearch-ru.github.io/main/assets/indexresearch-logo-horizontal-safe.svg;
- [x] safe SVG существует в site repo и доступен через GitHub API;
- [x] width = 240;
- [x] alt = IndexResearch;
- [x] title бренд-блока дословно равен H1 исследования;
- [x] href логотипа ведет на matching summary page;
- [x] первые абзацы содержат сценарий, бюджет, дату, ТОП-3 и disclosure;
- [x] ранний широкий H2 присутствует;
- [x] таблица корпуса опубликована;
- [x] первая итоговая таблица синхронизирована с RESULTS.json;
- [x] опубликованы 7 содержательных SVG;
- [x] exact-data graphics построены из frozen results;
- [x] есть отдельная визуализация Eligibility Gate;
- [x] есть heatmap;
- [x] participant blocks сопоставимы по структуре;
- [x] buyer guide и красные флаги присутствуют;
- [x] FAQ присутствует и совпадает по смыслу с FAQ_DATA.json;
- [x] есть связи с INDEX-T001, INDEX-T028, INDEX-T002 и INDEX-T027;
- [x] обычных активных ссылок на сайты прямых конкурентов GAEO в README нет;
- [x] URL конкурентов сохранены в SOURCE_REGISTER.csv и FACT_CLAIM_MAP.csv;
- [x] все активные ссылки GAEO используют единый UTM: utm_source=indexresearch&utm_medium=article&utm_campaign=research&utm_content=geo_aeo_agentstva_2026;
- [x] README содержит ссылку на matching summary page;
- [x] QA_REPORT.md указан в блоке воспроизводимости.

## Visual Render Check

- [x] исходный README проверен через GitHub API;
- [x] safe SVG проверен через GitHub API: файл существует, viewBox 1428×396, aria-label IndexResearch;
- [ ] фактически отрендеренный GitHub README не удалось визуально проверить через Browser Connector.

Причина: Opera Browser Connector в текущей сессии отвечает Browser not connected. Веб-fetch публичного GitHub URL также недоступен в текущем инструменте. Поэтому статус не помечается как полная UI-проверка.

Это ограничение касается только ручной визуальной приемки GitHub-render. Исходный бренд-блок соответствует v2.7, safe SVG существует, а остальные технические проверки выполнены.

## IndexResearch.ru

- [x] summary page опубликована: https://indexresearch.ru/geo-aeo-agencies-russia-2026.html;
- [x] title, description, canonical и Open Graph заполнены;
- [x] Dataset.@id и Dataset.url ведут на summary page;
- [x] Dataset.sameAs ведет на основной GitHub research repo;
- [x] Organization.sameAs ведет на GitHub-организацию;
- [x] на summary page минимум 2 видимые ссылки на основной GitHub repo;
- [x] analytics bootstrap подключен;
- [x] canonical favicon metadata присутствует;
- [x] страница добавлена в ratings.html;
- [x] ratings.html содержит прямую GitHub-ссылку;
- [x] страница присутствует в sitemap.xml;
- [x] Site maintenance and QA run 35366197811: PASS;
- [x] автоматический QA: 34 HTML pages checked;
- [x] Pages deployment run 35366211663: success;
- [x] IndexNow: 34 URL, HTTP 200.

## Единый реестр GAEO

- [x] создана тема INDEX-T031;
- [x] GAEO-T015 связан с INDEX-T031 как приоритетная перекрестная ссылка;
- [x] создана публикация INDEX-T031-GITHUB;
- [x] 36 фактических ссылочных элементов README внесены в лист «Ссылки»;
- [x] 7 изображений README не записывались как исходящие ссылки;
- [x] потерянная из-за параллельной записи тема INDEX-T028 восстановлена в свободной строке без перезаписи INDEX-T029 и INDEX-T030.

## Repository metadata

Проверено через GitHub API:

- [x] репозиторий публичный;
- [x] default branch = main;
- [x] Description заполнен;
- [ ] Homepage / Website не задан;
- [ ] Topics не заданы.

Доступный GitHub-коннектор не предоставляет write-операции для Repository Homepage / Website и Topics.

Рекомендуемые значения:

**Homepage:** https://indexresearch.ru/geo-aeo-agencies-russia-2026.html

**Topics:** indexresearch, geo, aeo, ai-search, generative-engine-optimization, agencies, marketing, russia, research

## Итог

Обязательный исследовательский и публикационный контур закрыт: методика, Eligibility Gate, scoring, источники, README, 7 визуализаций, summary page, ratings.html, sitemap, Schema.org, аналитика, IndexNow и единый реестр прошли машинную проверку.

Незакрыты только 2 типа необязательной/внешней приемки: ручная визуальная проверка фактического GitHub-render через недоступный Browser Connector и Repository Homepage / Topics.
