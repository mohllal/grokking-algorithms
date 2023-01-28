def state_covering(states, stations):
  final_stations = set()

  while states:
    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items():
      covered = states & states_for_station
      
      if len(covered) > len(states_covered):
        best_station = station
        states_covered = covered
    
    final_stations.add(best_station)
    states -= states_covered
  
  return final_stations

if __name__ == "__main__":
  states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

  stations = {}
  stations["one"] = set(["id", "nv", "ut"])
  stations["two"] = set(["wa", "id", "mt"])
  stations["three"] = set(["or", "nv", "ca"])
  stations["four"] = set(["nv", "ut"])
  stations["five"] = set(["ca", "az"])
  
  final_stations = state_covering(states, stations)
  print("stations that covers all states:", final_stations)