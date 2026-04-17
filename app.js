const tg = window.Telegram.WebApp;
tg.ready();

const user = tg.initDataUnsafe.user;

fetch("https://betgeniebot.onrender.com/auth/telegram", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(user)
});