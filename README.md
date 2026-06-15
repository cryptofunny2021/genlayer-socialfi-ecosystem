# GenLayer SocialFi Ecosystem

## 🚀 به‌روزرسانی اخیر (v0.2.3)
- Interaction Hub حالا مستقیماً به Reputation Scoring و Dynamic Token متصل شده.
- ثبت هر تعامل باعث افزایش Reputation و Mint توکن می‌شود.
- اکوسیستم در حال یکپارچه شدن است.

**آدرس قراردادها (ثابت):**
- Interaction Hub: `0xF4f25C67D8aaa24A71E85C9cCF61c5c1a8F2f8b1`
- Reputation Scoring: `0x58a73d1dC168B4BAdf5965758656d37d963e4a81`
- Dynamic Token: `0xeA166C0845904c919A5CD501465976B8d03dBfE6`
- 
A multi-contract SocialFi ecosystem built on GenLayer Testnet.

This project demonstrates how multiple smart contracts can work together to create a decentralized engagement, reputation, rewards, task management, and dispute resolution infrastructure.

---

# Ecosystem Overview

The ecosystem consists of five interconnected smart contracts:

### 1. Reputation Scoring

Tracks and stores user reputation based on participation and activity.

Contract ID:

0x58a73d1dC168B4BAdf5965758656d37d963e4a81

Repository:

https://github.com/cryptofunny2021/reputation_scoring

---

### 2. Dynamic Token

Manages token balances and reward distribution.

Contract ID:

0xeA166C0845904c919A5CD501465976B8d03dBfE6

Repository:

https://github.com/cryptofunny2021/dynamic_token

---

### 3. Dispute Resolution

Stores and manages dispute records in a transparent on-chain manner.

Contract ID:

0x4DEC89Af46EaB9cc54DDd6BCB037B3D16B97eb58

Repository:

https://github.com/cryptofunny2021/dispute_resolution

---

### 4. Interaction Hub

Records user interactions and engagement activity.

Contract ID:

0xF4f25C67D8aaa24A71E85C9cCF61c5c1a8F2f8b1

Repository:

https://github.com/cryptofunny2021/interaction_hub

---

### 5. Task Marketplace

Creates and manages user tasks.

Contract ID:

0x8d5359CCB96900Fde7fF94321a74188299984208

Repository:

https://github.com/cryptofunny2021/task_marketplace

---

# Architecture

User Activity
│
▼

Interaction Hub
│
▼

Reputation Scoring
│
▼

Dynamic Token

▲                   ▲
│                   │

Task Marketplace    Dispute Resolution

│                   │
└─────────┬─────────┘
▼

Reputation Updates

---

# Workflow

1. Users interact with the ecosystem.

2. Interactions are recorded by the Interaction Hub contract.

3. Reputation Scoring updates user reputation.

4. Dynamic Token distributes rewards based on participation.

5. Users create and manage tasks through Task Marketplace.

6. Disputes can be submitted and managed through Dispute Resolution.

7. Reputation can be influenced by dispute outcomes and ecosystem activity.

---

# Smart Contract Repositories

* https://github.com/cryptofunny2021/reputation_scoring

* https://github.com/cryptofunny2021/dynamic_token

* https://github.com/cryptofunny2021/dispute_resolution

* https://github.com/cryptofunny2021/interaction_hub

* https://github.com/cryptofunny2021/task_marketplace

---

# Network

GenLayer Bradbury Testnet

---

# Author

GitHub:
https://github.com/cryptofunny2021

Built for experimentation, ecosystem design, and decentralized application development on GenLayer.
