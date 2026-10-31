<p align="center">
  <a href="https://dyl521.github.io/"><img src="./assets/hero.svg" width="880" alt="Hi, I'm Yulin (DYL521), AI application engineer and Python backend developer, next to DeepSeek-chan, the whale-girl mascot, in a speech-bubble pose that changes every hour." /></a>
</p>

<p align="center">
  <a href="https://dyl521.github.io/"><img src="./assets/nav-website.svg" height="32" alt="Website" /></a>
  <a href="https://github.com/DYL521?tab=repositories"><img src="./assets/nav-repos.svg" height="32" alt="Repositories" /></a>
  <a href="mailto:1016068291@qq.com"><img src="./assets/nav-mail.svg" height="32" alt="Email" /></a>
</p>

<p align="center">
  <strong>Yulin Deng</strong> — AI application engineer, Python backend, 8 years in.<br />
  <sub>RAG, agents, enterprise integrations. Sharing what I build, learning from what you build.</sub>
</p>

## Selected work

> **[Jarvis Registry ↗](https://github.com/ascending-llc/jarvis-registry)** · Contributor<br />
> Enterprise MCP &amp; agent gateway.<br />
> Contributions: [embedding reindexing](https://github.com/ascending-llc/jarvis-registry/commit/cfa8267b5f57471544bce4a7e8b3ffe9ed05fb44) · [tool access controls](https://github.com/ascending-llc/jarvis-registry/commit/5ebe945115059765ab8d3da1b4422a62dbd15470)<br />
> <sub>Python · MCP · AI infrastructure</sub>

> **[Agentic Design Patterns CN ↗](https://github.com/DYL521/Agentic-Design-Patterns-CN)** · Learning resource<br />
> Agent design patterns with implementation examples, in Chinese and English.<br />
> <sub>AI agents · Design patterns · Chinese / English</sub>

## What I work on

| Focus | What I do |
| :--- | :--- |
| **RAG & knowledge** | End-to-end RAG: parsing, chunking, embedding, vector storage, retrieval, metadata filtering and cited answers. Query rewrite, intent detection, rerank and curated QA for messy enterprise docs. Multi-source sync (S3, Google Drive, SQL Server) with incremental, scheduled and manual modes.<br /><sub>LlamaIndex · LangChain · Weaviate · OpenAI · AWS Bedrock</sub> |
| **Agents & MCP** | LangGraph agents with checkpointed state and session recovery. MCP servers for Google Workspace and SQL Server. PromptOps: prompts versioned outside the app repo and loaded by release tag.<br /><sub>LangGraph · FastMCP · MySQL checkpointer · Docker Compose</sub> |
| **Backend & data** | Concurrent, network-heavy Python services and async task pipelines. MySQL indexing, transactions, locks, query tuning, sharding and disaster recovery. Redis cache penetration, breakdown and avalanche.<br /><sub>FastAPI · Django / DRF · Flask · Celery · MySQL · Redis</sub> |
| **Identity & access** | Domain account lifecycle across internal systems: onboarding / offboarding, AD sync, MFA, permission-change alerts, vendor accounts.<br /><sub>Spring Boot · Django · LDAP / AD · RocketMQ</sub> |
| **Workflow automation** | Jira Server / Data Center administration and extension, 100+ ScriptRunner Groovy scripts, custom REST endpoints, webhook → MQ integration across 10+ internal systems.<br /><sub>Groovy · ScriptRunner · Jira REST API · Elasticsearch</sub> |
| **AI-assisted engineering** | Turning AI coding from chat into repeatable workflow: repo-level skills, AGENTS.md / CLAUDE.md, review checklists, safe boundaries.<br /><sub>Claude Code · Codex · GitHub Copilot</sub> |

## Toolbox

| Area | Tools |
| :--- | :--- |
| Languages | `Python` `Java` `Go` `Groovy` `SQL` |
| LLM & AI | `LlamaIndex` `LangChain` `LangGraph` `FastMCP` `Weaviate` `OpenAI` `AWS Bedrock` `Prompt engineering` `Fine-tuning (LoRA)` |
| Backend | `FastAPI` `Django` `DRF` `Flask` `Celery` `Nameko` `Spring Boot` `MyBatis-Plus` |
| Data | `MySQL` `PostgreSQL` `Redis` `MongoDB` `Elasticsearch` |
| Messaging | `RabbitMQ` `RocketMQ` `Webhooks` |
| Cloud & infra | `Docker` `Docker Compose` `Kubernetes` `AWS` `Alibaba Cloud` `Git` |
| Integrations | `MCP` `LDAP / AD` `Jira` `Confluence` `ScriptRunner` `Feishu / Lark` `WeCom` `Google Workspace` `REST APIs` |

<details>
<summary><strong>中文介绍 · 展开阅读</strong></summary>

### 你好，我是玉林。欢迎交流，共同学习。

AI 应用工程师，Python 后端，8 年开发经验。关注 RAG、Agent 与企业系统集成。这里记录我参与的开源项目与整理的学习资料，欢迎交流技术思路，也期待从你的经历中学习。

**开源实践**

- **[Jarvis Registry](https://github.com/ascending-llc/jarvis-registry)**：企业 MCP 与 Agent 网关，参与 embedding 重建索引和工具访问控制等开发。
- **[Agentic Design Patterns CN](https://github.com/DYL521/Agentic-Design-Patterns-CN)**：整理 AI Agent 设计模式的中英文资料，结合概念与实现示例学习。

**工程方向**

- **RAG 与知识检索**：覆盖解析、分块、Embedding、向量存储、检索召回、元数据过滤、答案生成与可追溯引用的完整链路；针对“召回不准、答案无标准”的场景，结合 Query Rewrite、意图识别、Rerank 与标准 QA 库。支持 S3、Google Drive、SQL Server 等多源数据的增量、定时与手动同步。
  <br /><sub>LlamaIndex · LangChain · Weaviate · OpenAI · AWS Bedrock</sub>
- **Agent 与 MCP**：基于 LangGraph 构建 Agent，提供状态保存与会话恢复；封装 Google Workspace、SQL Server 的 MCP Server；PromptOps 让提示词独立于应用仓库管理，按 release tag 加载。
  <br /><sub>LangGraph · FastMCP · MySQL checkpointer · Docker Compose</sub>
- **后端与数据**：精通 Python，掌握并发编程与网络通信；深入理解 MySQL 索引、事务、锁机制，擅长 SQL 调优、分库分表与容灾；熟悉 Redis 线程模型，解决缓存穿透、击穿、雪崩问题。
  <br /><sub>FastAPI · Django / DRF · Flask · Celery · MySQL · Redis</sub>
- **身份与权限**：域账号全生命周期管理，覆盖入离职、AD 同步、MFA、权限变更预警和外采系统账号，连接内部系统，减少重复操作。
  <br /><sub>Spring Boot · Django · LDAP / AD · RocketMQ</sub>
- **协作流程自动化**：维护与扩展 Jira Server / Data Center，基于 ScriptRunner 开发 100+ Groovy 脚本，扩展 REST Endpoints，通过 Webhook → MQ 打通 10+ 内部系统。
  <br /><sub>Groovy · ScriptRunner · Jira REST API · Elasticsearch</sub>
- **AI 辅助工程**：把 AI Coding 从“聊天式问答”变成可复用的工程流程，沉淀仓库级 Skill、AGENTS.md / CLAUDE.md、review checklist 与安全边界。
  <br /><sub>Claude Code · Codex · GitHub Copilot</sub>

**工具箱**

| 领域 | 工具 |
| :--- | :--- |
| 语言 | `Python` `Java` `Go` `Groovy` `SQL` |
| 大模型与 AI | `LlamaIndex` `LangChain` `LangGraph` `FastMCP` `Weaviate` `OpenAI` `AWS Bedrock` `Prompt 工程` `模型微调（LoRA）` |
| 后端框架 | `FastAPI` `Django` `DRF` `Flask` `Celery` `Nameko` `Spring Boot` `MyBatis-Plus` |
| 数据 | `MySQL` `PostgreSQL` `Redis` `MongoDB` `Elasticsearch` |
| 消息 | `RabbitMQ` `RocketMQ` `Webhook` |
| 云与基础设施 | `Docker` `Docker Compose` `Kubernetes` `AWS` `阿里云` `Git` |
| 系统集成 | `MCP` `LDAP / AD` `Jira` `Confluence` `ScriptRunner` `飞书` `企业微信` `Google Workspace` `REST API` |

如果你也在探索这些方向，欢迎交流具体问题、讨论实现方案，一起学习进步。

[个人网站 ↗](https://dyl521.github.io/) · [代码仓库](https://github.com/DYL521?tab=repositories) · [邮件交流](mailto:1016068291@qq.com)

</details>

<p align="center"><img src="./assets/whale-divider.svg" width="280" alt="Wave divider with a small whale." /></p>
<p align="center">
  <strong>Let’s exchange ideas.</strong><br />
  <sub>RAG, backend engineering, or a problem you’re working through.</sub><br /><br />
  <a href="mailto:1016068291@qq.com">Email me</a> &nbsp; · &nbsp; <a href="https://dyl521.github.io/">Visit my website ↗</a>
</p>

<p align="center"><sub>DeepSeek-chan art: community fan art collected in <a href="https://github.com/the-beating-light-of-the-nail/deepseek-chan-meme-pack">deepseek-chan-meme-pack</a> (#050 and #123 by Zhihu artist @忻致知). A new pose every hour.</sub></p>
