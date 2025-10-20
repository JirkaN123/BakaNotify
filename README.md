# 📅 BakaNotify

Discord bot, který ti automaticky pošle rozvrh z Bakalářů do DM a připomene, co máš za chvíli za hodinu.

---

### 🚀 Funkce
- 📥 Stahuje veřejný rozvrh bez loginu
- 🔔 Denní notifikace v 22:00
- ⚙️ `/setup` pro nastavení vlastní třídy
- 💬 `/rozvrh` pro ruční vyžádání rozvrhu

---

### 💡 Instalace

```bash
git clone https://github.com/JirkaN123/BakaNotify.git
cd BakaNotify
pip install -r requirements.txt
copy .env.example .env
# Uprav .env s tvým Discord tokenem
python src/main.py