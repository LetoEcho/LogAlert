# LogAlert
Notify via Telegram of changes in a log of a remote machine via SSH

## How to create a Telegram Bot

1. Open Telegram and search for the user @BotFather.
2. Type /newbot and follow the instructions to:
    - Give your bot a name.
	- Choose a username (it must end with bot, like LogAlertaBot).
3. At the end, BotFather will give you an Access Token, something like:
`123456789:ABCdefGhIJklMnOpQRsTUvWxYZ1234567890`
4. Save that token. It will be used later.
5. Start the bot on Telegram.
6. Go to this link in a browser:
`https://api.telegram.org/bot<ACESS_TOKEN>/getUpdates`
Replace `<ACESS_TOKEN>` with the token given to you by BotFather. 
7. Something like this will appear:
<pre><code>{
  "ok": true,
  "result": [
    {
      "update_id": 123456789,
      "message": {
        "chat": {
          "id": 987654321,
          "first_name": "YOUR_NAME",
          ...
        },
        ...
      }
    }
  ]
}</code></pre>
Write down that `chat.id`, which is your Telegram Chat ID.