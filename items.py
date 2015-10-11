# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field


class DigikeyAllproductsItem(Item):
    
	Datasheet = Field()
	Image = Field()
	Digikey_Part_Number = Field()
	Product_link = Field()
	Manufacturer_Part_Number = Field()
	Part_Number_link = Field()
	Vendor = Field()
	Vendor_link = Field()
	Description = Field()
	Quantity_Available = Field()
	UnitPrice_USD = Field()
	Minimum_Quantity = Field()
	Packaging = Field()
	Series = Field()
	Core_Processor = Field()
	Core_Size = Field()
	Speed = Field()
	Connectivity = Field()
	Peripherals = Field()
	Number_of_IO = Field()
	Program_Memory_Size = Field()
	Program_Memory_Type = Field()
	EEPROM_Size = Field()
	RAM_Size = Field()
	Voltage_Supply = Field()
	Data_Converters = Field()
	Oscillator_Type = Field()
	Operating_Temperature = Field()
	Package_Case = Field()
	Supplier_Device_Package = Field()
