export default {
  async fetch(request, env) {
    if (request.method !== "POST") {
      return new Response("MMQR Easy Pay Bot Running");
    }

    try {
      const update = await request.json();

      if (!update.message) {
        return new Response("OK");
      }

      const chatId = update.message.chat.id;
      const text = update.message.text || "";

      if (text === "/start") {
        await sendMessage(
          env.BOT_TOKEN,
          chatId,
          "💸 MMQR Easy Pay\n\nMinimum: 500 MMK\nMaximum: 1,000,000 MMK\n\nပေးချေလိုသော ငွေပမာဏကို ရိုက်ထည့်ပါ။"
        );
      }

      return new Response("OK");

    } catch (err) {
      return new Response(`Error: ${err.message}`, {
        status: 500,
      });
    }
  },
};

async function sendMessage(token, chatId, text) {
  await fetch(
    `https://api.telegram.org/bot${token}/sendMessage`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        chat_id: chatId,
        text: text,
      }),
    }
  );
}
