/*
 * DFPLAYER_MINI.h
 *
 *  Created on: May 16, 2020
 *      Author: controllerstech
 */

#ifndef INC_DFPLAYER_MINI_H_
#define INC_DFPLAYER_MINI_H_

#include <stdint.h>

void Send_cmd (uint8_t cmd, uint8_t Parameter1, uint8_t Parameter2);
void DF_PlayFromStart(void);
void DF_Init (uint8_t volume);
void DF_Next (void);
void DF_Pause (void);
void DF_Previous (void);
void DF_Playback (void);
void DF_Playspecific(uint16_t song);
void DF_Stop(void);
void Check_Key (void);
uint8_t Check_Busy(void);
void DF_SetAmplifier(uint8_t amplifier);


#define IS_WORKING 0
#define STANDBY 1
#endif /* INC_DFPLAYER_MINI_H_ */
