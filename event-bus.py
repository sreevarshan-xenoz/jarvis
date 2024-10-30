import asyncio
import logging
from typing import Any

class EventBus:
    """Central event management system"""
    def __init__(self):
        self.subscribers = {}
        self.queue = asyncio.Queue()
        self._running = True

    async def publish(self, event_type: str, data: Any):
        """Publish an event to all subscribers"""
        await self.queue.put((event_type, data))

    async def subscribe(self, event_type: str, callback):
        """Subscribe to an event type"""
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    async def start(self):
        """Start processing events"""
        while self._running:
            try:
                event_type, data = await self.queue.get()
                if event_type in self.subscribers:
                    for callback in self.subscribers[event_type]:
                        await callback(data)
            except Exception as e:
                logging.error(f"Error processing event: {str(e)}")
