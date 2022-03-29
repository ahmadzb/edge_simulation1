class Task:
    def __init__(self, size: int, workload: int, nodeId: int, arrivalTime: float, hopLimit: int = 2) -> None:
        self._size = size
        self._workload = workload
        self._nodeId = nodeId
        self._arrivalTime = arrivalTime
        self._hopLimit = hopLimit
    
    def setup(self, id: int) -> None:
        self._id = id
        
    def id(self):
        return self._id
    def size(self):
        return self._size
    def workload(self):
        return self._workload
    def nodeId(self):
        return self._nodeId
    def arrivalTime(self):
        return self._arrivalTime
    def hopLimit(self):
        return self._hopLimit
    def setHopLimit(self, hopLimit):
        self._hopLimit = hopLimit
    
    def __str__(self) -> str:
        return ("Task//id:" + str(self._id) + " size:" + str(self._size) +
                " workload:" + str(self._workload) + " nodeId:" + str(self._nodeId) +
                " arrivalTime:" + str(self._arrivalTime) + " hopLimit:" + str(self._hopLimit))