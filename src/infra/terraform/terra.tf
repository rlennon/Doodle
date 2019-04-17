# Doodlesoft infrastructure deployment
# this will create doodle application infrastructure
# see README for instructions

# setup login details
provider "vsphere" {
  user           = "${var.vsphere_user}"
  password       = "${var.vsphere_password}"
  vsphere_server = "${var.vsphere_server}"

  allow_unverified_ssl = true
}

data "vsphere_datacenter" "dc" {
  name = "ha-datacenter"
}

data "vsphere_datastore" "datastore" {
  name          = "${var.vsphere_datastore}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_resource_pool" "pool" {
  name          = "${var.vsphere_pool}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_network" "network" {
  name          = "${var.vsphere_network}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

# here we copy premade ubuntu disk image
resource "vsphere_file" "vmdk-01" {
  datacenter = "${data.vsphere_datacenter.dc.name}"
  datastore = "${data.vsphere_datastore.datastore.name}"
  source_datacenter = "${data.vsphere_datacenter.dc.name}"
  source_datastore = "${data.vsphere_datastore.datastore.name}"
  create_directories = "true"
  source_file = "${var.vsphere_source_file}"
  destination_file = "/doodle-api/disk0.vmdk"
}

resource "vsphere_file" "vmdk-02" {
  datacenter = "${data.vsphere_datacenter.dc.name}"
  datastore = "${data.vsphere_datastore.datastore.name}"
  source_datacenter = "${data.vsphere_datacenter.dc.name}"
  source_datastore = "${data.vsphere_datastore.datastore.name}"
  create_directories = "true"
  source_file = "${var.vsphere_source_file}"
  destination_file = "/doodle-web/disk0.vmdk"
}

resource "vsphere_file" "vmdk-03" {
  datacenter = "${data.vsphere_datacenter.dc.name}"
  datastore = "${data.vsphere_datastore.datastore.name}"
  source_datacenter = "${data.vsphere_datacenter.dc.name}"
  source_datastore = "${data.vsphere_datastore.datastore.name}"
  create_directories = "true"
  source_file = "${var.vsphere_source_file}"
  destination_file = "/doodle-api-stage/disk0.vmdk"
}

resource "vsphere_file" "vmdk-04" {
  datacenter = "${data.vsphere_datacenter.dc.name}"
  datastore = "${data.vsphere_datastore.datastore.name}"
  source_datacenter = "${data.vsphere_datacenter.dc.name}"
  source_datastore = "${data.vsphere_datastore.datastore.name}"
  create_directories = "true"
  source_file = "${var.vsphere_source_file}"
  destination_file = "/doodle-web-stage/disk0.vmdk"
}


# here we create VMs
resource "vsphere_virtual_machine" "doodle-api" {
  name             = "doodle-api"
  resource_pool_id = "${data.vsphere_resource_pool.pool.id}"
  datastore_id     = "${data.vsphere_datastore.datastore.id}"

  num_cpus = 2
  memory   = 1024
  guest_id = "ubuntu64Guest"

  network_interface {
    network_id = "${data.vsphere_network.network.id}"
  }
  disk {
    label = "disk0"
    attach = true
    path = "/doodle-api/disk0.vmdk"
    datastore_id     = "${data.vsphere_datastore.datastore.id}"
 }
}

resource "vsphere_virtual_machine" "doodle-web" {
  name             = "doodle-web"
  resource_pool_id = "${data.vsphere_resource_pool.pool.id}"
  datastore_id     = "${data.vsphere_datastore.datastore.id}"

  num_cpus = 2
  memory   = 1024
  guest_id = "ubuntu64Guest"

  network_interface {
    network_id = "${data.vsphere_network.network.id}"
  }
  disk {
    label = "disk0"
    attach = true
    path = "/doodle-web/disk0.vmdk"
    datastore_id     = "${data.vsphere_datastore.datastore.id}"
  }
}

resource "vsphere_virtual_machine" "doodle-web-stage" {
  name             = "doodle-web-stage"
  resource_pool_id = "${data.vsphere_resource_pool.pool.id}"
  datastore_id     = "${data.vsphere_datastore.datastore.id}"

  num_cpus = 2
  memory   = 1024
  guest_id = "ubuntu64Guest"

  network_interface {
    network_id = "${data.vsphere_network.network.id}"
  }
  disk {
    label = "disk0"
    attach = true
    path = "/doodle-web-stage/disk0.vmdk"
    datastore_id     = "${data.vsphere_datastore.datastore.id}"
  }
}

resource "vsphere_virtual_machine" "doodle-api-stage" {
  name             = "doodle-api-stage"
  resource_pool_id = "${data.vsphere_resource_pool.pool.id}"
  datastore_id     = "${data.vsphere_datastore.datastore.id}"

  num_cpus = 2
  memory   = 1024
  guest_id = "ubuntu64Guest"

  network_interface {
    network_id = "${data.vsphere_network.network.id}"
  }
  disk {
    label = "disk0"
    attach = true
    path = "/doodle-api-stage/disk0.vmdk"
    datastore_id     = "${data.vsphere_datastore.datastore.id}"
  }
}
