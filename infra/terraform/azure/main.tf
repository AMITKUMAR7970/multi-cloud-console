provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = "hybrid-cloud-rg"
  location = var.location
}

resource "azurerm_linux_virtual_machine" "app" {
  name                  = "hybrid-cloud-app"
  resource_group_name   = azurerm_resource_group.main.name
  location              = azurerm_resource_group.main.location
  size                  = var.vm_size
  admin_username        = var.admin_username
  network_interface_ids = []
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}

output "vm_id" {
  value = azurerm_linux_virtual_machine.app.id
}