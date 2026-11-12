---
title: 首頁
description: 講講講講小學堂：一個概念，一頁講義。
hide:
  - navigation
  - toc
---

<div class="kk-hero" markdown>
<h1 class="kk-title"><span>講</span><span class="kk-echo-2">講</span><span class="kk-echo-3">講</span><span class="kk-echo-4">講</span><span class="kk-rest">小學堂</span></h1>
<svg class="kk-wave" viewBox="0 0 540 60" role="presentation" aria-hidden="true"><path d="M0 30.0 L4 20.5 L8 13.2 L12 9.2 L16 8.9 L20 12.2 L24 18.3 L28 26.0 L32 33.9 L36 40.7 L40 45.2 L44 47.0 L48 45.7 L52 41.9 L56 36.3 L60 30.0 L64 24.1 L68 19.5 L72 17.0 L76 16.8 L80 18.8 L84 22.7 L88 27.5 L92 32.4 L96 36.7 L100 39.5 L104 40.6 L108 39.9 L112 37.5 L116 34.0 L120 30.0 L124 26.3 L128 23.4 L132 21.8 L136 21.7 L140 23.0 L144 25.4 L148 28.4 L152 31.5 L156 34.2 L160 36.0 L164 36.7 L168 36.2 L172 34.7 L176 32.5 L180 30.0 L184 27.7 L188 25.9 L192 24.9 L196 24.8 L200 25.6 L204 27.1 L208 29.0 L212 31.0 L216 32.6 L220 33.8 L224 34.2 L228 33.9 L232 32.9 L236 31.6 L240 30.0 L244 28.5 L248 27.4 L252 26.8 L256 26.7 L260 27.2 L264 28.2 L268 29.4 L272 30.6 L276 31.6 L280 32.4 L284 32.6 L288 32.4 L292 31.8 L296 31.0 L300 30.0 L304 29.1 L308 28.4 L312 28.0 L316 28.0 L320 28.3 L324 28.9 L328 29.6 L332 30.4 L336 31.0 L340 31.5 L344 31.6 L348 31.5 L352 31.2 L356 30.6 L360 30.0 L364 29.4 L368 29.0 L372 28.7 L376 28.7 L380 28.9 L384 29.3 L388 29.8 L392 30.2 L396 30.6 L400 30.9 L404 31.0 L408 31.0 L412 30.7 L416 30.4 L420 30.0 L424 29.6 L428 29.4 L432 29.2 L436 29.2 L440 29.3 L444 29.6 L448 29.8 L452 30.1 L456 30.4 L460 30.6 L464 30.6 L468 30.6 L472 30.5 L476 30.2 L480 30.0 L484 29.8 L488 29.6 L492 29.5 L496 29.5 L500 29.6 L504 29.7 L508 29.9 L512 30.1 L516 30.3 L520 30.4 L524 30.4 L528 30.4 L532 30.3 L536 30.2 L540 30.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
<p class="kk-lead">一個概念，一頁講義。本站以學術報告的形式整理訊號處理、統計與模型選擇、訊號偵測，以及相似度量測的核心概念。每篇講義都包含定義、推導、圖解、Python 實作與參考文獻。</p>
</div>

## 講義

<div class="kk-grid" markdown>

<div class="kk-card" markdown>
<p class="kk-card-label"><span class="kk-card-no">第 1 講</span><span class="kk-card-cat">訊號處理</span></p>
<p class="kk-card-title" markdown="span">[離散小波轉換（DWT）](signal-processing/dwt.md)</p>
<p class="kk-card-desc">以濾波器組逐層分解訊號，取得兼具時間與頻率資訊的近似與細節係數。</p>
<ul class="kk-chips"><li>10 條公式</li><li>2 張圖</li><li>前置：無</li></ul>
<p class="kk-card-action" markdown="span">[開始閱讀](signal-processing/dwt.md){ .md-button }</p>
</div>

<div class="kk-card" markdown>
<p class="kk-card-label"><span class="kk-card-no">第 2 講</span><span class="kk-card-cat">訊號處理</span></p>
<p class="kk-card-title" markdown="span">[小波封包分解（WPD）](signal-processing/wpd.md)</p>
<p class="kk-card-desc">同時分解近似與細節係數，得到均勻劃分的頻帶與能量特徵。</p>
<ul class="kk-chips"><li>7 條公式</li><li>2 張圖</li><li>前置：DWT</li></ul>
<p class="kk-card-action" markdown="span">[開始閱讀](signal-processing/wpd.md){ .md-button }</p>
</div>

<div class="kk-card" markdown>
<p class="kk-card-label"><span class="kk-card-no">第 3 講</span><span class="kk-card-cat">統計與模型選擇</span></p>
<p class="kk-card-title" markdown="span">[Akaike 資訊準則（AIC）](model-selection/aic.md)</p>
<p class="kk-card-desc">以對數概似與參數數量的權衡，在候選模型中選出預測能力最佳者。</p>
<ul class="kk-chips"><li>8 條公式</li><li>1 張圖</li><li>前置：無</li></ul>
<p class="kk-card-action" markdown="span">[開始閱讀](model-selection/aic.md){ .md-button }</p>
</div>

<div class="kk-card" markdown>
<p class="kk-card-label"><span class="kk-card-no">第 4 講</span><span class="kk-card-cat">訊號偵測</span></p>
<p class="kk-card-title" markdown="span">[AIC picker：起始點偵測](signal-detection/aic-picker.md)</p>
<p class="kk-card-desc">將訊號切為雜訊段與訊號段，以 AIC 最小值估計暫態訊號的起始時間。</p>
<ul class="kk-chips"><li>3 條公式</li><li>1 張圖</li><li>前置：AIC</li></ul>
<p class="kk-card-action" markdown="span">[開始閱讀](signal-detection/aic-picker.md){ .md-button }</p>
</div>

<div class="kk-card" markdown>
<p class="kk-card-label"><span class="kk-card-no">第 5 講</span><span class="kk-card-cat">相似度與距離</span></p>
<p class="kk-card-title" markdown="span">[餘弦相似性](similarity/cosine-similarity.md)</p>
<p class="kk-card-desc">以兩向量夾角的餘弦衡量方向一致程度，常用於特徵向量比對。</p>
<ul class="kk-chips"><li>6 條公式</li><li>1 張圖</li><li>前置：無</li></ul>
<p class="kk-card-action" markdown="span">[開始閱讀](similarity/cosine-similarity.md){ .md-button }</p>
</div>

<div class="kk-card kk-card-more">
<p>更多講義，陸續加入中</p>
</div>

</div>

## 建議閱讀順序

本站講義彼此相關，以下兩條路線可依需求選讀。

**路線一：小波分析與特徵比對**

1. [離散小波轉換（DWT）](signal-processing/dwt.md)：理解多解析度分析與濾波器組。
2. [小波封包分解（WPD）](signal-processing/wpd.md)：把高頻區域也細分，取得頻帶能量特徵。
3. [餘弦相似性](similarity/cosine-similarity.md)：比較不同時間點的能量特徵向量。

**路線二：模型選擇與起始點偵測**

1. [Akaike 資訊準則（AIC）](model-selection/aic.md)：理解配適度與模型複雜度的權衡。
2. [AIC picker：起始點偵測](signal-detection/aic-picker.md)：把同一個準則應用在訊號分段上。

## 每篇講義的結構

所有講義遵循相同的章節順序，方便對照閱讀：

1. 摘要
2. 背景與動機
3. 數學定義與推導
4. 圖解與範例
5. Python 實作
6. 應用實例
7. 限制與注意事項
8. 相關講義
9. 參考文獻
