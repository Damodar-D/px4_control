#!/usr/bin/env python

import triad_openvr
import numpy as np
import time


class VRController:
	def __init__(self):
		self.pose = None # [x,y,z](m)
		self.orient = None # Euler angles
		self.vr = triad_openvr.triad_openvr()

	def position(self):
		"""
		return: [x,y,z]
		"""
		pose = self.vr.devices["controller_1"].get_pose_euler()
		time.sleep(0.01)
		try:
			self.pose = np.array(pose[:3])
		except TypeError:
			pass

		return self.pose

	def orientation(self):
		"""
		return: [yaw,pitch,roll]
		"""
		pose = self.vr.devices["controller_1"].get_pose_euler()
		time.sleep(0.01)
		self.orient = np.array(pose[3:])
		return self.orient
