require "ttt"

describe Board do
	it "contains list of 9 board places" do
		board = Board.new
		board.make_board.should == [1..9]
		end
end

describe Player do

end