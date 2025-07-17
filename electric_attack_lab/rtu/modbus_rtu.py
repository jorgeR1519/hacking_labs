from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

block = ModbusSequentialDataBlock(0, [100]*100)
store = ModbusSlaveContext(hr=block)
context = ModbusServerContext(slaves=store, single=True)

identity = ModbusDeviceIdentification()
identity.VendorName = 'VulnerableRTU'
identity.ProductCode = 'RTU'
StartTcpServer(context, identity=identity, address=("0.0.0.0", 502))
