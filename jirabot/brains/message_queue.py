from cachetools import TTLCache

events_inflight = TTLCache(maxsize=1000, ttl=60)

def event_queued_or_recent(event_id):
    return events_inflight.get(event_id) is not None

def enqueue_event(event_id):
    events_inflight[event_id] = 1
