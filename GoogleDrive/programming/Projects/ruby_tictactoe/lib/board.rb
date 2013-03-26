class Board
	def make_board
		board = (1...10).to_a
		board { |num| board[num].to_s }
	end
end