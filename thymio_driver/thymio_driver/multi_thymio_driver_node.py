from typing import Any

import rclpy
import rclpy.executors

from .manager import Manager
from .thymio_driver_node import ThymioDriver


class ThymioManager(Manager):  # type: ignore

    _drivers = {'thymio-II': ThymioDriver}


def main(args: Any = None) -> None:
    rclpy.init(args=args)
    executor = rclpy.executors.SingleThreadedExecutor()
    manager = ThymioManager(executor)
    executor.spin()
    manager.destroy_node()
    rclpy.shutdown()
