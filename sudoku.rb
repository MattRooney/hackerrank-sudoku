def n_i;$<.readlines.map{|r|r.split.map(&:to_i)};end
def c?(c);c.all?{|d|d.inject(:+)==45};end
def b_b(i);i.each_slice(3).to_a.map{|rs|rs.map{|s|s.each_slice(3).to_a.map{|r|r}}.transpose.map(&:flatten)}.flatten(1);end
def p_r(r);$>.write(r ? "Valid\n" : "Invalid\n");end
x = n_i;x.shift.first.between?(1,10)||p_r(false);x.each_slice(9){|b|p_r(c?(b)&&c?(b.transpose)&&c?(b_b(b)))}
