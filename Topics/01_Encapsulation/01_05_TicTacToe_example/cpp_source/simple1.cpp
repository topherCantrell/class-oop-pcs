enum PLAYER {
    PLAYER_1, PLAYER_2
};

enum CELL {
    CELL_0, CELL_1, CELL_2, CELL_3, CELL_4
};

enum BOARD_STATUS {
    PLAYING, TIE, WON_1, WON_2
};

int ask_for_move(bool is_player_1) {
    return 0;
}

int ask_for_move(int player_num) {
    return 0;
}

int ask_for_move(PLAYER player) {
    return 0;
}

void place_token(int cell_num, int player_num) {
}

int get_board_status() {
    return -1; // Still going
    return 0; // Tie
    return 1; // Player 1 won
    return 2; // Player 2 won
}

bool check_for_win() {
    return false;
}

bool has_open_spaces() {
    return true;
}

void print_board() {

    int move = ask_for_move(1);
    int move = ask_for_move(true);
    int move = ask_for_move(PLAYER_1);

}
