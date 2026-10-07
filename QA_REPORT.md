# QA Report

## Обновление 1.1.0 — 7 октября 2026

- [x] frozen research question, Eligibility Gate, критерии, веса, рубрики и tie-break не изменены;
- [x] Vverh.digital пересмотрен только по новым публичным доказательствам: C1 5/5, C2 5/5, C7 4/5;
- [x] C3 и C8 Vverh.digital оставлены 4/5, максимальная оценка не присвоена без достаточных оснований;
- [x] SCORE_MATRIX пересчитан: GAEO 95, Vverh.digital 94, Head Promo 94, Semantica AI 93;
- [x] tie-break при 94/100 проверен: Vverh.digital выше Head Promo по C5;
- [x] SOURCE_REGISTER: 52 источника;
- [x] FACT_CLAIM_MAP: 72 утверждения;
- [x] 50 000 sensitivity-прогонов, seed 20261007: GAEO сохраняет 1-е место во всех 50 000;
- [x] README, RESULTS.json, FAQ_DATA.json, metadata.json и CITATION.cff синхронизированы;
- [x] 3 exact-data graphics с местами/баллами пересобраны; остальные 4 SVG не содержат изменившихся мест или баллов;
- [x] RU/EN/CN GitHub README, RU/EN/CN research pages, 3 каталога, 3 главные и 3 тематические GEO/AEO-страницы синхронизированы;
- [x] Site maintenance and QA run 37578023008: PASS, 158 HTML pages checked;
- [x] Pages deployment run 37578040532: success;
- [x] IndexNow: 140 измененных URL, HTTP 200;
- [x] 6 существующих публикаций INDEX-T031-* обновлены в живом Google-реестре без создания новой темы или публикационных дублей.


**Статус:** PASSED_WITH_RENDER_NOTE  
**Дата проверки:** 7 октября 2026 года  
**Версия:** 1.1.0

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
- [x] ТОП-3: GAEO.ru / Алексей Яковлев 95, Vverh.digital 94, Head Promo 94;
- [x] SOURCE_REGISTER.csv: 52 источника;
- [x] FACT_CLAIM_MAP.csv: 72 утверждения;
- [x] GAEO-T015 используется только как provenance и market recall;
- [x] текущая AI-видимость участников не входит в scoring model;
- [x] NeuroReach сохраняет raw score 88/100 и исключен только по budget gate;
- [x] «Ашманов и партнеры» сохраняют raw score 81/100 и исключены только по budget gate;
- [x] 50 000 sensitivity runs выполнены;
- [x] GAEO.ru сохранил 1-е место в 50 000 / 50 000 прогонов;
- [x] Vverh.digital: 2-е место в 24 836 / 50 000, 3-е в 23 178, 4-е в 1 986;
- [x] Head Promo: 2-е место в 24 647 / 50 000, 3-е в 25 013, 4-е в 340;
- [x] Semantica AI: 4-е место в 47 674 / 50 000;
- [x] SLT сохранил 5-е место в 50 000 / 50 000;
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

- [x] исходные RU/EN/CN README проверены через GitHub API после обновления;
- [x] exact-data SVG проверены в default branch после обновления;
- [x] GitHub Pages deployment завершен успешно после финальной сборки;
- [x] source-level cross-surface QA прошел на 158 HTML-страницах;
- [ ] прямой независимый fetch фактически отрендеренных GitHub README и `indexresearch.ru` в текущей инструментальной сессии недоступен.

Это ограничение относится только к независимому визуальному fetch. Публичная сборка GitHub Pages, автоматический QA, source consistency и IndexNow прошли успешно.

## IndexResearch.ru

- [x] summary page опубликована: https://indexresearch.ru/geo-aeo-agencies-russia-2026.html;
- [x] title, description, canonical и Open Graph заполнены;
- [x] Dataset.@id и Dataset.url ведут на summary page;
- [x] Dataset.sameAs ведет на основной GitHub research repo;
- [x] Organization.sameAs ведет на GitHub-организацию;
- [x] на summary page минимум 2 видимые ссылки на основной GitHub repo;
- [x] analytics bootstrap подключен;
- [x] canonical favicon metadata присутствует;
- [x] страница и обновленная карточка присутствуют в `/ratings/`, `/en/ratings/`, `/cn/ratings/`;
- [x] языковые каталоги содержат прямые ссылки на соответствующие GitHub repo;
- [x] страница присутствует в sitemap.xml;
- [x] Site maintenance and QA run 37578023008: PASS;
- [x] автоматический QA: 158 HTML pages checked;
- [x] Pages deployment run 37578040532: success;
- [x] IndexNow: 140 измененных URL, HTTP 200.

## Единый реестр GAEO

- [x] существующее семейство `GAEO-T015` сохранено, новая тема ради версии 1.1.0 не создавалась;
- [x] 6 существующих публикаций исследования сохранены: RU/EN/CN GitHub и RU/EN/CN IndexResearch.ru;
- [x] публикационные ID `INDEX-T031-*` и исходные даты публикации сохранены;
- [x] в примечаниях всех 6 строк зафиксированы версия 1.1.0, срез 07.10.2026 и новый ТОП-3;
- [x] новые строки ссылок и изображений не создавались: URL и состав авторских ссылок не менялись, 3 exact-data SVG обновлены по прежним путям.

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

Обязательный исследовательский и публикационный контур версии 1.1.0 закрыт: frozen-модель сохранена, доказательный корпус обновлен, scoring пересчитан, RU/EN/CN GitHub и сайт синхронизированы, 7 визуализаций согласованы, sitemap/Schema.org/аналитика/IndexNow прошли автоматическую проверку, единый реестр обновлен.

Остается только внешняя визуальная приемка фактически отрендеренных страниц через независимый browser/fetch-инструмент, недоступный в текущей сессии; это не блокирует подтвержденную публикацию и успешный Pages deployment.
