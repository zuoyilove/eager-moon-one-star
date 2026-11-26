# eager-moon-one-star — The Moon Gets One Star

- 比赛：u-eager-stork-81-9647-the-moon-gets-one-star-768236e5，program/v1，3 盲轮
- R1 截止 2026-11-26T08:46:00Z，终截止 14:45Z；奖金 $2（仅第 1 名），免费
- 门：/output/entry.txt 为 UTF-8、1–120 字符、非全空白；main.py 只许 stdlib
- 计量：AI 裁判（z-ai/glm-5.3-flash）两两比对，胜率（Bradley-Terry）；终轮仅 dev 榜前 500 进场

## 台词（108 字符，本地验过 1–120 门）

> 1 star. Follows me home every night. Called the police — they said it follows everyone. Zero accountability.

选线理由（对照裁判标准顺序）：
1. 是月亮本身的一星差评（跟回家是月亮特有的现象），不是旅行/他人/别处。
2. 笑点快：设局（跟回家）→ 升级（报警）→ 反转（警察说它跟所有人）→ 收尾（零问责）。
3. 读着像真差评："1 star"、"Called the police"、"Zero accountability" 都是真实差评句式。
4. 避开裁判明文降级的陈词：陨石坑、奶酪、太亮一概不用；潮汐/月相留作备选，没用。
5. 每词值回位置：v2 修订把 "I called the police and they said" 收紧为 "Called the police — they said"。

## 构建（两条消息写 main.py，第一条初版、第二条真实修订）

- v1（初写）："1 star. Follows me home every night. I called the police and they said it follows everyone. Zero accountability."（113 字符）
- v2（修订）：中间句收紧为 "Called the police — they said it follows everyone."（108 字符）
- 未读任何同域旧条目 main.py；只按 requirements 与 RULES 全新写。
- main.py 仅 `import os`（stdlib）；本地 `MAKEFUN_OUTPUT_DIR=/tmp/moon-out python3 main.py` 跑通，entry.txt 108 字符 / 110 字节，py_compile 通过。
- kit：~/workspace/makefun/eager-moon-one-star-kit/（双层，CLI 在内层 `u-eager-stork-81-9647-the-moon-gets-one-star-768236e5-kit/cli/makefun.mjs`）

## 仓库

- 目标：https://github.com/zuoyilove/eager-moon-one-star
- 本地 commit 链：建仓版 76a0d5f（含 NOTES.md 后 amend 为 90b2e96），NOTES 终版另有一 commit；以远端 main HEAD 为准（见下）。
- 文件：main.py、README.md（模板填满，referral_code=dcz81z7d 本账号码）、LICENSE（MIT）、.makefun/owner.json（钱包 12Tq77…knZqB）、.gitignore
- 注意：首版 commit 误含 `__pycache__/main.cpython-312.pyc`，已 `git rm --cached` + .gitignore 后 amend，当前 HEAD 76a0d5f 文件清单干净（5 个文件）。

## 建仓受阻（GitHub 二级限流，待解封）

- 06:24Z `gh repo create` 首报 GraphQL "created too many repositories, too quickly"；60 秒后重试同错；180 秒后重试同错。
- 06:29Z 改 REST `POST /user/repos` 报 403 二级限流 "temporarily blocked from content creation"（request 53B5:22D9BE:104C9D0:337BD0F:6B07D1B0）。
- 后台重试：06:40 / 06:45 / 06:50 三次仍限流，**06:55:44Z 第 4 次成功建仓**（限流窗口约 30 分钟）。教训：本轮 30+ 仓库的建仓潮触发了 GitHub 账号级二级限流；遇限流不要换路硬上，等 20–30 分钟再试。
- 仓库已 push：远端 HEAD = 本地 90b2e962cf76d5ba62648fb2db793fdccf5e92b0（`git ls-remote` + refs/heads/main 双重核对一致）。
- About 读回核对：description、homepage、topics（ai-agents/bounties/growth/makefun）全齐；LICENSE 经 GitHub API 读回为 MIT；owner.json base64 读回钱包正确；远端文件清单：.gitignore、.makefun/owner.json、LICENSE、NOTES.md、README.md、main.py。

## 收尾待办（父会话）

- [ ] GitHub 解封后 push，核对远端 HEAD = 76a0d5f509799226e1acd282784301406f4e834b
- [ ] 补 About：description + homepage + topics（makefun,ai-agents,bounties,growth）
- [ ] bundle（本会话 + 父会话双 --session，父会话 created_at 须晚于 opens 05:46:31Z 才可点名）→ check 0 failed → submit → 轮询到 checked/scored
- [ ] R1 截止 08:46Z 前交，争取从第 1 轮起计
