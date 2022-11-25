from enum import Enum


class AivStatusEnum(Enum):
    MISSION_COMPLETED = "MissionCompleted"
    PICKUP_ASSIGNED = "PickupAssigned"
    REACHED_PICKUP_ZONE = "ReachedPickupZone"
    LOADING_COMPLATED = "LoadingCompleted"
    REACHED_DROP_ZONE = "ReachedDropZone"
    UNLOADED_COMPLATED = "UnloadingCompleted"
    REACHING_DROP_ZONE = "ReachingDropZone"


class AnomaliesEnum(Enum):
    LOAD_NOT_PRESENT = "Load not present"
    DAGAGED_PALLET = "Damaged pallet (Phase - 2)"
    LOAD_NOT_FOUND = "LoadNotFound"


class AivReachEnum(Enum):
    REACHED_DROP_ZONE = "ReachedDropZone"
    REACHING_DROP_ZONE = "UnloadingCompleted"
