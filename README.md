# Meow

## Introduction

When run, this python script will determine if it needs to
send a reminder email. Written for feline weight management.

## Usage

### Command Line

```console
Usage: fatcats.py [OPTIONS]

  Sends an email if a reminder is needed.

Options:
  -c, --config TEXT  Location of YAML config file.  [default: meowstamp.yaml]
  -d, --debug
  --smtp_url TEXT    Default SMTP URL.  [default: localhost]
  --help             Show this message and exit.
```

### meowstamp.yaml

```yaml
last_fed: 2019-09-29 06:00:00.00000
period: 30.0 # hours
subject: 'Feed the Cats'
message: 'Feed the cats!'
from: 'meow@example.com'
to:
  - name: "Kittenmaster"
    user: "kittenmaster"
    domain: "example.com"
```
