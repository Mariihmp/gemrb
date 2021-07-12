/* GemRB - Infinity Engine Emulator
 * Copyright (C) 2003 The GemRB Project
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 *
 */

#ifndef SDLVIDEODRIVER_H
#define SDLVIDEODRIVER_H

#include "Video/Video.h"

#include "GUI/EventMgr.h"

#include "DPadSoftKeyboard.h"
#include "SDLSurfaceDrawing.h"
#include "SDLSurfaceSprite2D.h"

#include <vector>

namespace GemRB {

#if SDL_VERSION_ATLEAST(1,3,0)
#define SDL_SRCCOLORKEY SDL_TRUE
#define SDL_SRCALPHA 0
#define SDLKey SDL_Keycode
#define SDL_JoyAxisEvent SDL_ControllerAxisEvent
#define SDL_JoyButtonEvent SDL_ControllerButtonEvent
#define SDLK_SCROLLOCK SDLK_SCROLLLOCK
#define SDLK_KP1 SDLK_KP_1
#define SDLK_KP2 SDLK_KP_2
#define SDLK_KP3 SDLK_KP_3
#define SDLK_KP4 SDLK_KP_4
#define SDLK_KP6 SDLK_KP_6
#define SDLK_KP7 SDLK_KP_7
#define SDLK_KP8 SDLK_KP_8
#define SDLK_KP9 SDLK_KP_9
#else
	using SDL_Keycode = Sint32;
#endif

inline int GetModState(int modstate)
{
	int value = 0;
	if (modstate&KMOD_SHIFT) value |= GEM_MOD_SHIFT;
	if (modstate&KMOD_CTRL) value |= GEM_MOD_CTRL;
	if (modstate&KMOD_ALT) value |= GEM_MOD_ALT;
	return value;
}

class SDLVideoDriver : public Video {
public:
	SDLVideoDriver(void);
	~SDLVideoDriver(void) override;
	int Init(void) override;

	Holder<Sprite2D> CreateSprite(const Region& rgn, void* pixels, const PixelFormat&) override;

	void BlitSprite(const Holder<Sprite2D> spr, const Region& src, Region dst,
					BlitFlags flags, Color tint = Color()) override;
	void BlitGameSprite(const Holder<Sprite2D> spr, const Point& p, BlitFlags flags, Color tint = Color()) override;

protected:
#if SDL_VERSION_ATLEAST(1,3,0)
	using vid_buf_t = SDL_Texture;
	using sprite_t = SDLTextureSprite2D;
#else
	using vid_buf_t =SDL_Surface;
	using sprite_t = SDLSurfaceSprite2D;
	using SDL_Point = Point;
#endif
	VideoBufferPtr scratchBuffer; // a buffer that the driver can do with as it pleases for intermediate work

	int CreateDriverDisplay(const char* title) override;

	virtual vid_buf_t* ScratchBuffer() const = 0;
	virtual inline vid_buf_t* CurrentRenderBuffer() const=0;
	virtual inline vid_buf_t* CurrentStencilBuffer() const=0;
	Region CurrentRenderClip() const;
	
	BlitFlags RenderSpriteVersion(const SDLSurfaceSprite2D* spr, BlitFlags renderflags, const Color* = NULL);

	virtual void BlitSpriteRLEClipped(const Holder<Sprite2D> spr, const Region& src, const Region& dst, BlitFlags flags = BlitFlags::NONE, const Color* tint = NULL)=0;
	virtual void BlitSpriteNativeClipped(const sprite_t* spr, const SDL_Rect& src, const SDL_Rect& dst, BlitFlags flags = BlitFlags::NONE, const SDL_Color* tint = NULL)=0;
	void BlitSpriteClipped(const Holder<Sprite2D> spr, Region src, const Region& dst, BlitFlags flags = BlitFlags::NONE, const Color* tint = NULL);

	int PollEvents() override;
	/* used to process the SDL events dequeued by PollEvents or an arbitraty event from another source.*/
	virtual int ProcessEvent(const SDL_Event & event);
	void Wait(uint32_t w) override { SDL_Delay(w); }

private:
	virtual int CreateSDLDisplay(const char* title) = 0;
	virtual void DrawSDLPoints(const std::vector<SDL_Point>& points, const SDL_Color& color, BlitFlags flags = BlitFlags::NONE)=0;

	void DrawCircleImp(const Point& origin, unsigned short r, const Color& color, BlitFlags flags) override;
	void DrawEllipseSegmentImp(const Point& origin, unsigned short xr, unsigned short yr, const Color& color,
							   double anglefrom, double angleto, bool drawlines, BlitFlags flags) override;
public:
	// static functions for manipulating surfaces
	static bool SetSurfacePalette(SDL_Surface* surf, const SDL_Color* pal, int numcolors = 256);
};

}

#endif
