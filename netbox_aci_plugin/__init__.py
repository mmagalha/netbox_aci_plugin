"""Top-level package for NetBox ACI Plugin."""

__author__ = """Martin Hauser"""
__email__ = "git@pheus.dev"
__version__ = "0.0.11"


from netbox.plugins import PluginConfig


class ACIConfig(PluginConfig):
    """NetBox ACI Plugin specific configuration."""

    name = "netbox_aci_plugin"
    verbose_name = "NetBox ACI"
    description = "NetBox plugin for documenting Cisco ACI specific objects."
    version = __version__
    author = __author__
    author_email = __email__
    base_url = "aci"
    min_version = "4.2.0"
    max_version = "4.3.99"
    default_settings = {
        "create_default_aci_tenants": True,
        "create_default_aci_contracts_filters": True,
    }


config = ACIConfig
