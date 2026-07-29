---
layout: page
permalink: /troubleshooting/
title: "MSR X6 Troubleshooting: Driver, USB and Bluetooth Fixes"
description: "Fix common MSR X6 and MSRX6BT software installation, USB detection, Bluetooth pairing, and card-reading problems."
schema_type: "TechArticle"
---

## Device not detected by USB

1. Use a data-capable cable, not a charge-only cable.
2. Connect directly to another USB port.
3. Restart the application and operating system.
4. Check Device Manager on Windows or System Information on macOS.
5. Reinstall the correct package once after removing an incomplete installation.

## Bluetooth device not found

- Confirm the model is MSRX6BT/Bluetooth.
- Disconnect it from other phones or computers.
- Enable the app's Bluetooth/nearby-device permission.
- Pair through the app if required rather than the system settings screen.
- Power-cycle the device and retry nearby.

## Software opens but cannot communicate

- Close other applications that may hold the USB or Bluetooth connection.
- Match the application to the hardware model and operating system.
- Avoid USB hubs and virtual-machine passthrough during diagnosis.
- Try a clean, non-sensitive test card to separate connection and media problems.

## Swipe/read errors

Inspect the media and card path, use a steady swipe, and verify that the intended track format matches your authorized test system. Repeated failures across known-good test media may indicate hardware service is required.

When contacting the seller or manufacturer, provide the exact model, operating-system version, application version, connection type, and error message—never send real card data.
