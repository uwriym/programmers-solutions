# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling)
  include_hash = { 'aya': 0, 'ye': 0, 'woo': 0, 'ma': 0 }
  answer = 0
  babbling.each do |bab|
    # bab에 include_hash의 key가 하나라도 있다면
    if include_hash[bab]
      include_hash.each do |word|
        include_hash[word] += 1 if bab.include? word
      end
    end
  end
  return answer
end

input = ["aya", "yee", "u", "maa", "wyeoo"]
puts solution(input)