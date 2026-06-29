import flet as ft
import requests
import json

def main(page: ft.Page):
    page.title = "Automation Control Hub"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # 1. Your Make.com Webhook URL
    WEBHOOK_URL = "https://hook.make.com/your-unique-webhook-id-goes-here"

    def fire_automation(e):
        trigger_btn.text = "Sending..."
        trigger_btn.disabled = True
        page.update()

        payload = {"source": "flet_mobile_app", "action": "run_workflow"}
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
            if response.status_code == 200:
                status_text.value = "Success: Workflow Triggered!"
                status_text.color = ft.colors.GREEN
            else:
                status_text.value = "Error: Failed to reach Make.com"
                status_text.color = ft.colors.RED
        except Exception as ex:
            status_text.value = f"Connection Error: {ex}"
            status_text.color = ft.colors.RED

        trigger_btn.text = "Trigger Workflow"
        trigger_btn.disabled = False
        page.update()

    # UI Elements
    header = ft.Text("Make.com Automations", size=24, weight=ft.FontWeight.BOLD)
    status_text = ft.Text("Waiting for input...", italic=True)
    
    trigger_btn = ft.ElevatedButton(
        text="Trigger Workflow",
        icon=ft.icons.ROCKET_LAUNCH,
        on_click=fire_automation,
        style=ft.ButtonStyle(padding=20)
    )

    # Add elements to the screen
    page.add(
        header,
        ft.Divider(height=20, color="transparent"),
        trigger_btn,
        ft.Divider(height=10, color="transparent"),
        status_text
    )

if __name__ == "__main__":
    # Runs the app natively
    ft.app(target=main)