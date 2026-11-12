# 講講講講小學堂

一個以學術報告形式撰寫的概念小講義網站：**一個概念 = 一頁講義**。目前收錄訊號處理、統計與模型選擇、訊號偵測、相似度與距離四個分類，共 5 篇講義：

- 離散小波轉換（DWT）
- 小波封包分解（WPD）
- Akaike 資訊準則（AIC）
- AIC picker：起始點偵測
- 餘弦相似性

網站以 MkDocs + Material for MkDocs 建置，透過 GitHub Actions 自動部署到 GitHub Pages。所有寫作與新增內容的規則都記載在 [`AGENTS.md`](AGENTS.md)。

## 專案結構

```
AGENTS.md                  給 AI 與協作者的專案規則
mkdocs.yml                 網站設定與導覽目錄
requirements.txt           建置網站所需套件
templates/                 新講義模板
scripts/figures/           產生講義圖片的 Python 腳本
docs/                      網站內容（Markdown）
.github/workflows/         自動部署設定
```

## 本機預覽

```bash
pip install -r requirements.txt
mkdocs serve                 # 瀏覽 http://127.0.0.1:8000
mkdocs build --strict        # 檢查是否有失效連結或設定錯誤
```

重新產生圖片：

```bash
pip install -r scripts/figures/requirements.txt
cd scripts/figures
python dwt.py                # 其他講義依此類推
```

## 部署到 GitHub Pages

1. 在 GitHub 建立新的公開 repository，例如 `jiangjiang-xuetang`。
2. 將本專案推送到 `main` 分支。
3. 進入 repository 的 **Settings → Pages**，將 **Source** 設為 **GitHub Actions**。
4. 到 **Actions** 分頁確認 `Deploy to GitHub Pages` 執行成功，網址為 `https://<帳號>.github.io/jiangjiang-xuetang/`。
5. （選用）將網址填入 `mkdocs.yml` 的 `site_url` 與 `repo_url`。

## 新增一篇講義

對 AI 說明要新增的主題，並請它先閱讀 `AGENTS.md`。規則中的「新增講義的標準流程」與「完成前檢查清單」會引導它完成建檔、套用模板、產生圖片、更新目錄與首頁卡片、補上相關連結，最後以 `mkdocs build --strict` 驗證。

---

## 作業繳交資訊

1. **專案簡介**：講講講講小學堂是一個跨主題的概念講義網站，以學術報告格式整理訊號處理與資料分析的核心概念，每篇講義包含摘要、數學推導、圖解、Python 實作、應用、限制與參考文獻。
2. **GitHub Repository**：`https://github.com/<帳號>/jiangjiang-xuetang`
3. **網頁連結**：`https://<帳號>.github.io/jiangjiang-xuetang/`
4. **規則檔**：[`AGENTS.md`](AGENTS.md)
5. **規則如何幫助 AI 繼續完成新內容**：`AGENTS.md` 把「一個概念 = 一頁講義」轉成可執行的規則，包括固定的章節順序、檔名與圖片放置位置、公式與參考文獻格式、全站用語表，以及新增講義的逐步流程（建檔 → 套模板 → 產生圖片 → 更新目錄與首頁卡片 → 補上雙向連結 → 嚴格建置驗證）。之後只要請 AI「新增一篇關於 OOO 的講義」，它讀完規則就知道內容要怎麼寫、檔案放在哪裡、還要同步更新哪些地方；`mkdocs build --strict` 也會自動擋下失效連結與遺漏的連結，讓新內容與既有頁面保持一致。
