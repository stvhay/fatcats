"""Module contains email handling."""
import email.message
import smtplib


class EmailError(Exception):
    """Error during email handling occurred."""
    pass


def send_email(conf, url):
    """Send the email reminder."""
    try:
        with smtplib.SMTP(url) as s:
            msg = email.message.EmailMessage()
            msg['From'] = conf.from_address
            msg['To'] = conf.to_addresses
            msg['Subject'] = conf.subject
            msg.set_content('{}\n\nLast reminder sent {}.'.format(conf.message, conf.last_fed))
            s.send_message(msg)
    except Exception as e:
        raise EmailError("Error sending email.") from e
