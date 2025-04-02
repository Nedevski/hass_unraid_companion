# Unraid Companion

![Last release](https://img.shields.io/github/release-date/nedevski/hass_unraid_companion?style=flat-square)
![Code size](https://img.shields.io/github/languages/code-size/nedevski/hass_unraid_companion?style=flat-square)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/nedevski/tip)

> ## **WARNING:** This integration is a work in progress. Expect buggy behaviour and install on your own risk.

## Installation

### HACS (Recommended)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=nedevski&repository=hass_unraid_companion&category=integration)

### Manual

1. Copy the `unraid_companion` folder into your `custom_components` directory.
2. Restart Home Assistant.
3. Go to Configuration > Integrations.
4. Click the "+ ADD INTEGRATION" button.
5. Search for "Unraid Companion" and select it.
6. Follow the configuration steps.

## Configuration

Check the [Unraid API Documentation](https://docs.unraid.net/API/cli/)

### CLI Cheatsheet

- `unraid-api start`

- `unraid-api apikey --create`

### Integration configuration

- `host` - The IP/host of your Unraid instance
  - Currently only HTTPS connection supported
  - Use the format `192.168.XXX.XXX` - do **NOT** put the `http://` or `https://`
- `api_key` - The API Key created in the previous step
