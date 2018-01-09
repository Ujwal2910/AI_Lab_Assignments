import java.io.IOException;	

 class JealousHusbands {
	public static void main(String[] args) throws IOException {

		
		boolean WifeAOnLeftBank = true;
		boolean WifeBOnLeftBank = true;
		boolean WifeCOnLeftBank = true;
		boolean BoatOnLeftBank = true;
		boolean Husband1OnLeftBank = true;
		boolean Husband2OnLeftBank = true;
		boolean Husband3OnLeftBank = true;

		while (WifeAOnLeftBank || WifeBOnLeftBank || WifeCOnLeftBank || BoatOnLeftBank || Husband1OnLeftBank
				|| Husband2OnLeftBank || Husband3OnLeftBank) {
			// Variables that represent an attempt at a move
			// (attempted state of the world)
			// Initialize to existing state of the world

			boolean tryWifeAOnLeftBank = WifeAOnLeftBank;
			boolean tryWifeBOnLeftBank = WifeBOnLeftBank;
			boolean tryWifeCOnLeftBank = WifeCOnLeftBank;
			boolean tryBoatOnLeftBank = BoatOnLeftBank;
			boolean tryHusband1OnLeftBank = Husband1OnLeftBank;
			boolean tryHusband2OnLeftBank = Husband2OnLeftBank;
			boolean tryHusband3OnLeftBank = Husband3OnLeftBank;

			System.out.println("Wife A is on the " + (WifeAOnLeftBank ? "left" : "right") + " side of the river");
			System.out.println("Wife B is on the " + (WifeBOnLeftBank ? "left" : "right") + " side of the river");
			System.out.println("Wife C is on the " + (WifeCOnLeftBank ? "left" : "right") + " side of the river");
			System.out.println("Husband 1 is on the " + (Husband1OnLeftBank ? "left" : "right") + " side of the river");
			System.out.println("Husband 2 is on the " + (Husband2OnLeftBank ? "left" : "right") + " side of the river");
			System.out.println("Husband 3 is on the " + (Husband3OnLeftBank ? "left" : "right") + " side of the river");
			System.out.println("Boat is on the " + (BoatOnLeftBank ? "left" : "right") + " side of the river");
			System.out.println("First Person who should go into the boat (a, 1, b, 2, c, 3) ");

			int Move1 = System.in.read();
			while (System.in.read() != '\n')
				;

			if ((Move1 == 'a' || Move1 == 'b' || Move1 == 'c' || Move1 == '1' || Move1 == '2' || Move1 == '3')) {

			} else {
				System.out.println("Invalid value!");
				continue;
			}

			System.out.println("Second Person who should go into the boat (a, 1, b, 2, c, 3) ");

			int Move2 = System.in.read();
			while (System.in.read() != '\n')
				; // throw away characters until new line

			if ((Move2 == 'a' || Move2 == 'b' || Move2 == 'c' || Move2 == '1' || Move2 == '2' || Move2 == '3')) {

			} else {
				System.out.println("Invalid value!");
				continue;

			}
			if (Move1 == 'a' || Move2 == 'a') {
				// Attempt to move the Wife A
				// First, check to see if they
				// are on the same side of the river

				if (WifeAOnLeftBank != BoatOnLeftBank) {
					System.out.println("Wife A must be on same side of river as the boat!");
					continue;
				}
				tryWifeAOnLeftBank = !tryWifeAOnLeftBank;

			}
			if (Move1 == 'b' || Move2 == 'b') {
				// Attempt to move the Wife B and Boat
				// First, check to see if they are on the same side
				if (WifeBOnLeftBank != BoatOnLeftBank) {
					System.out.println("Wife B must be on same side of river as the boat!");
					continue;
				}

				tryWifeBOnLeftBank = !tryWifeBOnLeftBank;

			}
			if (Move1 == 'c' || Move2 == 'c') {
				// Attempt to move the Wife C and Boat
				// First, check to see if they are on the same side
				if (WifeCOnLeftBank != BoatOnLeftBank) {
					System.out.println("Wife C must be on same side of river as the boat!");
					continue;
				}

				tryWifeCOnLeftBank = !tryWifeCOnLeftBank;

			}
			if (Move1 == '1' || Move2 == '1') {
				// Attempt to move the Husband 1 and Boat
				// First, check to see if they are on the same side
				if (Husband1OnLeftBank != BoatOnLeftBank) {
					System.out.println("Husband 1 must be on same side of river as the boat!");
					continue;
				}

				tryHusband1OnLeftBank = !tryHusband1OnLeftBank;

			}
			if (Move1 == '2' || Move2 == '2') {
				// Attempt to move the Husband 2 and Boat
				// First, check to see if they are on the same side
				if (Husband2OnLeftBank != BoatOnLeftBank) {
					System.out.println("Husband 2 must be on same side of river as the boat!");
					continue;
				}

				tryHusband2OnLeftBank = !tryHusband2OnLeftBank;

			}
			if (Move1 == '3' || Move2 == '3') {
				// Attempt to move the Husband 3 and Boat
				// First, check to see if they are on the same side
				if (Husband3OnLeftBank != BoatOnLeftBank) {
					System.out.println("Husband 3 must be on same side of river as the boat!");
					continue;
				}

				tryHusband3OnLeftBank = !tryHusband3OnLeftBank;

				// At this point, we need to validate that the new
				// attempt works out and husbands do not feel jealous.

			}
			if (tryWifeAOnLeftBank != tryHusband1OnLeftBank && ((tryWifeAOnLeftBank == tryHusband2OnLeftBank)
					|| (tryWifeAOnLeftBank == tryHusband3OnLeftBank))) {
				// This will make the Husband 1 Jealous.
				// If Wife A is not on the same side of Husband 1 and on
				// same side as Husband 2 or Husband 3.
				System.out.println("This move would make Husband 1 Jealous");
				continue;
			}
			if (tryWifeBOnLeftBank != tryHusband2OnLeftBank
					&& (tryWifeBOnLeftBank == tryHusband1OnLeftBank || tryWifeBOnLeftBank == tryHusband3OnLeftBank)) {
				// This will make the Husband 2 Jealous.
				// If Wife A is not on the same side of Husband 2 and on
				// same side as Husband 1 or Husband 3.
				System.out.println("This move would make Husband 2 Jealous");
				continue;
			}
			if (tryWifeCOnLeftBank != tryHusband3OnLeftBank
					&& (tryWifeCOnLeftBank == tryHusband1OnLeftBank || tryWifeCOnLeftBank == tryHusband2OnLeftBank)) {
				// This will make the Husband 3 Jealous.
				// If Wife A is not on the same side of Husband 3 and on
				// same side as Husband 1 or Husband 2.
				System.out.println("This move would make Husband 3 Jealous");
				continue;

			} else {
				// Move was successful. Copy the "try" world back into
				// the real world.

				WifeAOnLeftBank = tryWifeAOnLeftBank;
				WifeBOnLeftBank = tryWifeBOnLeftBank;
				WifeCOnLeftBank = tryWifeCOnLeftBank;
				BoatOnLeftBank = !BoatOnLeftBank;
				Husband1OnLeftBank = tryHusband1OnLeftBank;
				Husband2OnLeftBank = tryHusband2OnLeftBank;
				Husband3OnLeftBank = tryHusband3OnLeftBank;
			}
		}
        
		
		System.out.println("You won!");
	}
}
