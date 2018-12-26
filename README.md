## Requirement
- Installed python
- Installed pipenv

## Instalation
```bash
$ git clone https://github.com/uddinmtm/sms-sender.git
$ cd sms-sender
$ pipenv install
```

### Set credentials
```bash
$ cp .env.example .env
```

Fill your credential from zenziva sms gateway

## Run
You can run with
```bash
$ pipenv shell
$ python main.py notifications
```
And you can send new message with
```bash
$ echo '{"to":"08123456789","msg":"Hei broo!"}' >> notifications
```
