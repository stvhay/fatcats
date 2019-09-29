#!/usr/bin/env python3
"""Module to send periodic email reminders."""
import datetime
import logging
import click

from fatcats.common.configuration import Configuration, ConfigurationError
from fatcats.common.send_email import send_email, EmailError


@click.command()
@click.option('-c', '--config', default='meowstamp.yaml', help='Location of YAML config file.', show_default=True)
@click.option('-d', '--debug', is_flag=True)
@click.option('--smtp_url', default='localhost', help='Default SMTP URL.', show_default=True)
def meow(config_file, debug, smtp_url):
    """Sends a reminder if conditions are met."""
    try:
        logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
        conf = Configuration().load(config_file)
        now = datetime.datetime.now()
        if now - conf.last_fed > conf.period:
            send_email(conf, smtp_url)
            conf.last_fed = now
            conf.save(config_file)
            logging.info("Meowminder sent.")
        else:
            logging.debug("It is not time to send a reminder yet.")
    except (ConfigurationError, EmailError) as e:
        logging.error(e.message)
