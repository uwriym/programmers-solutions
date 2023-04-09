# https://school.programmers.co.kr/learn/courses/30/lessons/178871

# 도전 중 (테스트 9 ~ 13 시간초과 실패)

def solution(players, callings)

  callings.each do |call|
    overtaker_idx = players.index(call)
    players[overtaker_idx], players[overtaker_idx - 1] = players[overtaker_idx - 1], players[overtaker_idx]
  end

  return players
end

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

pp solution(players, callings)

# result = ["mumu", "kai", "mine", "soe", "poe"]