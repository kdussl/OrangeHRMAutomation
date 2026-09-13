import allure


def attach_screenshot(page, name):
    """
    Capture the current browser page and attach it to Allure.
    """
    try:
        allure.attach(
            page.screenshot(
                full_page=True
            ),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as error:
        print(f"Unable to attach screenshot '{name}': {error}")