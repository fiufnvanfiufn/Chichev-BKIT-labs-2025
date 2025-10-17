ActiveWorkers = {}

class Storage:
    def AddWorcer(self, user_id: int, username: str) -> bool:
        if user_id in ActiveWorkers:
            return False

        ActiveWorkers[user_id] = username

    def remove_worker(self, user_id: int) -> bool:
        if user_id in ActiveWorkers:
            del ActiveWorkers[user_id]
            return True
        return False

    def IsSomeoneWorking(self):
        return len(ActiveWorkers) > 0
