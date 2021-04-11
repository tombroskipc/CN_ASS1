import sys
from time import time
HEADER_SIZE = 12

class RtpPacket:	
	header = bytearray(HEADER_SIZE)
	
	def __init__(self):
		pass
		
	def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
		"""Encode the RTP packet with header fields and payload."""
		timestamp = int(time())
		header = bytearray(HEADER_SIZE)
		#--------------
		# TO COMPLETE
		#--------------
		# Fill the header bytearray with RTP header fields
		
		# header[0] = ...c
		# ...
		# TODO [encode each bit]
		header[0] =			    version << 6				# Version 1 bit
		header[0] = header[0] | padding << 5				# Padding 1 bit
		header[0] = header[0] | extension << 4				# eXtension 2 bits
		header[0] = header[0] | cc 							# Contribute Source 4 bits
		header[1] = 			  marker << 7				# Marker 1 bits
		header[1] = header[1] | pt  						# Payload Type 7 bits
		header[2] = 			seqnum >> 8			 		# SEQuence NUMber 16 bits (first 8 bits)
		header[3] = 			seqnum & 0xff 	 			# SEQuence NUMber 16 bits (last 8 bits)
		header[4] = 			timestamp >> 24				# timespamp 32 bits (first 8 bits)
		header[5] = 			(timestamp >> 16) & 0xFF 	# timespamp 32 bits (second 8 bits)
		header[6] =			    (timestamp >> 8) & 0xFF 	# timespamp 32 bits (third 8 bits)
		header[7] = 			timestamp & 0xFF 			# timespamp 32 bits (last 8 bits)
		header[8] = 			ssrc >> 24 					# Synchronization SouRCe (first 8 bits)
		header[9] = 			ssrc >> 16 & 0xFF;			# Synchronization SouRCe (second 8 bits)
		header[10] = 			ssrc >> 8 & 0xFF;			# Synchronization SouRCe (third 8 bits)
		header[11] = 			ssrc & 0xFF  				# Synchronization SouRCe (last 8 bits)

		self.header = header
		
		# Get the payload from the argument
		# self.payload = ...
		self.payload = payload


	def decode(self, byteStream):
		"""Decode the RTP packet."""
		self.header = bytearray(byteStream[:HEADER_SIZE])
		self.payload = byteStream[HEADER_SIZE:]
	
	def version(self):
		"""Return RTP version."""
		return int(self.header[0] >> 6)
	
	def seqNum(self):
		"""Return sequence (frame) number."""
		seqNum = self.header[2] << 8 | self.header[3]
		return int(seqNum)
	
	def timestamp(self):
		"""Return timestamp."""
		timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
		return int(timestamp)
	
	def payloadType(self):
		"""Return payload type."""
		pt = self.header[1] & 127
		return int(pt)
	
	def getPayload(self):
		"""Return payload."""
		return self.payload
		
	def getPacket(self):
		"""Return RTP packet."""
		return self.header + self.payload