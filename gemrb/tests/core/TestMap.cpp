/* GemRB - Infinity Engine Emulator
* Copyright (C) 2024 The GemRB Project
*
* This program is free software; you can redistribute it and/or
* modify it under the terms of the GNU General Public License
* as published by the Free Software Foundation; either version 2
* of the License, or (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program; if not, write to the Free Software
* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
*
*/

#include "../../core/GameData.h"
#include "../../core/Interface.h"
#include "../../core/InterfaceConfig.h"
#include "../../core/Map.h"
#include "../../core/PluginMgr.h"
#include "../../core/SaveGameMgr.h"

#include <gtest/gtest.h>

namespace GemRB {

class MapTest : public testing::Test {
public:
	static const Interface* gemrb;
	static const Map* map;

	// set up core and the first map from the demo
	static void SetUpTestSuite()
	{
		const char* argv[] = { "tester", "-c", "../../../demo/tester.cfg" };
		auto cfg = LoadFromArgs(3, const_cast<char**>(argv));
		gemrb = new Interface(std::move(cfg));

		auto gamStream = gamedata->GetResourceStream("gem-demo", IE_GAM_CLASS_ID);
		auto gamMgr = GetImporter<SaveGameMgr>(IE_GAM_CLASS_ID, gamStream);
		Game* game = gamMgr->LoadGame(new Game(), 0);
		core->SetGame(game);

		ResRef mapRef { "ar0100" };
		map = game->GetMap(mapRef, false);
	}

	static void TearDownTestSuite()
	{
		// cleanup to prevent a delay and crash on exit
		delete core->GetGame();
		core->SetGame(nullptr);
		VideoDriver.reset();
		delete gemrb;
	}
};

const Map* MapTest::map = nullptr;
const Interface* MapTest::gemrb = nullptr;

static Point badPaths[] = { Point(1270, 640), Point(1071, 699), Point(1170, 967), Point(1126, 601) };
static Point goodPaths[] = { Point(1126, 601), Point(685, 655), Point(720, 496), Point(1056, 336) };

TEST_F(MapTest, GetBlockedInLineTest1)
{
	// same point
	EXPECT_TRUE(map->IsVisibleLOS(badPaths[0], badPaths[0], nullptr));

	// random points
	for (int i = 0; i < 3; i++) {
		EXPECT_FALSE(map->IsVisibleLOS(badPaths[i], badPaths[i + 1], nullptr)) << "i: " << i << std::endl;

		EXPECT_TRUE(map->IsVisibleLOS(goodPaths[i], goodPaths[i + 1], nullptr)) << "i: " << i << std::endl;
	}
}

}
