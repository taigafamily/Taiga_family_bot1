==> Cloning from https://github.com/taigafamily/Taiga_family_bot1
==> Checking out commit a7c953fb03189272665dca69c919d202003a2cf0 in branch main
==> Using Python version 3.13.4 (default)
==> Docs on specifying a Python version: https://render.com/docs/python-version
==> Using Poetry version 2.1.3 (default)
==> Docs on specifying a Poetry version: https://render.com/docs/poetry-version
==> Running build command 'pip install -r requirements.txt'...
Collecting python-telegram-bot==20.8 (from -r requirements.txt (line 1))
  Downloading python_telegram_bot-20.8-py3-none-any.whl.metadata (15 kB)
Collecting python-dotenv (from -r requirements.txt (line 2))
  Downloading python_dotenv-1.1.1-py3-none-any.whl.metadata (24 kB)
Collecting httpx~=0.26.0 (from python-telegram-bot==20.8->-r requirements.txt (line 1))
  Downloading httpx-0.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting anyio (from httpx~=0.26.0->python-telegram-bot==20.8->-r requirements.txt (line 1))
  Downloading anyio-4.9.0-py3-none-any.whl.metadata (4.7 kB)
Collecting certifi (from httpx~=0.26.0->python-telegram-bot==20.8->-r requirements.txt (line 1))
  Downloading certifi-2025.7.9-py3-none-any.whl.metadata (2.4 kB)
Collecting httpcore==1.* (from httpx~=0.26.0->python-telegram-bot==20.8->-r requirements.txt (line 1))
  Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting idna (from httpx~=0.26.0->python-telegram-bot==20.8->-r requirements.txt (line 1))
  Downloading idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting sniffio (from httpx~=0.26.0->python-telegram-bot==20.8->-r requirements.txt (line 1))
  Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx~=0.26.0->python-telegram-bot==20.8->-r requirements.txt (line 1))
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Downloading python_telegram_bot-20.8-py3-none-any.whl (604 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 604.9/604.9 kB 23.4 MB/s eta 0:00:00
Downloading httpx-0.26.0-py3-none-any.whl (75 kB)
Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
Downloading python_dotenv-1.1.1-py3-none-any.whl (20 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading anyio-4.9.0-py3-none-any.whl (100 kB)
Downloading idna-3.10-py3-none-any.whl (70 kB)
Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Downloading certifi-2025.7.9-py3-none-any.whl (159 kB)
Installing collected packages: sniffio, python-dotenv, idna, h11, certifi, httpcore, anyio, httpx, python-telegram-bot
Successfully installed anyio-4.9.0 certifi-2025.7.9 h11-0.16.0 httpcore-1.0.9 httpx-0.26.0 idna-3.10 python-dotenv-1.1.1 python-telegram-bot-20.8 sniffio-1.3.1
==> Uploading build...
==> Uploaded in 3.3s. Compression took 0.9s
==> Build successful 🎉
==> Deploying...
==> Running 'sh start.sh'
Traceback (most recent call last):
  File "/opt/render/project/src/bot.py", line 78, in <module>
    main()
    ~~~~^^
  File "/opt/render/project/src/bot.py", line 70, in main
    app = ApplicationBuilder().token(TOKEN).build()
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/telegram/ext/_applicationbuilder.py", line 303, in build
    bot: Bot = self._build_ext_bot()  # build a bot
               ~~~~~~~~~~~~~~~~~~~^^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/telegram/ext/_applicationbuilder.py", line 265, in _build_ext_bot
    return ExtBot(
        token=self._token,
    ...<9 lines>...
        local_mode=DefaultValue.get_value(self._local_mode),
    )
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/telegram/ext/_extbot.py", line 224, in __init__
    super().__init__(
    ~~~~~~~~~~~~~~~~^
        token=token,
        ^^^^^^^^^^^^
    ...<6 lines>...
        local_mode=local_mode,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/telegram/_bot.py", line 255, in __init__
    raise InvalidToken("You must pass the token you received from https://t.me/Botfather!")
telegram.error.InvalidToken: You must pass the token you received from https://t.me/Botfather!
==> Exited with status 1
==> Common ways to troubleshoot your deploy: https://render.com/docs/troubleshooting-deploys
==> Running 'sh start.sh'
Traceback (most recent call last):
  File "/opt/render/project/src/bot.py", line 78, in <module>
    main()
    ~~~~^^
  File "/opt/render/project/src/bot.py", line 70, in main
    app = ApplicationBuilder().token(TOKEN).build()
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/telegram/ext/_applicationbuilder.py", line 303, in build
    bot: Bot = self._build_ext_bot()  # build a bot
               ~~~~~~~~~~~~~~~~~~~^^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/telegram/ext/_applicationbuilder.py", line 265, in _build_ext_bot
    return ExtBot(
        token=self._token,
    ...<9 lines>...
        local_mode=DefaultValue.get_value(self._local_mode),
    )
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/telegram/ext/_extbot.py", line 224, in __init__
    super().__init__(
    ~~~~~~~~~~~~~~~~^
        token=token,
        ^^^^^^^^^^^^
    ...<6 lines>...
        local_mode=local_mode,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/opt/render/project/src/.venv/lib/python3.13/site-packages/telegram/_bot.py", line 255, in __init__
    raise InvalidToken("You must pass the token you received from https://t.me/Botfather!")
telegram.error.InvalidToken: You must pass the token you received from https://t.me/Botfather!
