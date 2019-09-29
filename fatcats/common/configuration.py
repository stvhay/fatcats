"""Module holds configuration object."""
import attr
import email.headerregistry
import yaml


class ConfigurationError(Exception):
    """An error has occurred."""
    pass


@attr.s
class Configuration(object):
    """Holds configuration data."""
    last_fed = attr.ib(init=False)
    message = attr.ib(init=False)
    subject = attr.ib(init=False)
    period = attr.ib(init=False)
    _from_address = attr.ib(init=False)
    _to_addresses = attr.ib(init=False)

    @staticmethod
    def _convert_address(addr):
        """Converts an address dictionary to an email address."""
        try:
            return email.headerregistry.Address(*(addr[k] for k in ('name', 'user', 'domain')))
        except Exception as e:
            raise ConfigurationError("Error during address conversion.") from e

    def load(self, config_file):
        """Load a config file."""
        try:
            with open(config_file) as f:
                data = yaml.safe_load(f)
                self.last_fed = data['last_fed']
                self.message = data['message']
                self.subject = data['subject']
                self._from_address = data['from']
                self._to_addresses = data['to']
                return self
        except Exception as e:
            raise ConfigurationError("Error during load.") from e

    def save(self, config_file):
        """Save a config file."""
        try:
            with open(config_file, 'w') as f:
                yaml.dump(
                    {
                        'last_fed': self.last_fed,
                        'message': self.message,
                        'subject': self.subject,
                        'from': self._from_address,
                        'to': self._to_addresses
                    },
                    f,
                    default_flow_style=False)
        except Exception as e:
            raise ConfigurationError("Error during save.") from e

    def from_address(self):
        """Convert from address to Address."""
        return self._convert_address(self._from_address)

    def to_addresses(self):
        """Convert to addresses to an Address generator."""
        return (self._convert_address(addr) for addr in self._to_addresses)
