#!/usr/bin/env python
# -*- encode: utf-8 -*-

#MIT License (MIT)

#Copyright (c) <2014> <Rapp Project EU>

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

# Authors: Aris Thallas
# contact: aris.thallas@gmail.com

import os
from scipy.io import wavfile


class TransformAudio:


    def transform_audio(self, source_type, source_name, \
            target_type, target_name, target_channels, target_rate ):


        try:
            self.assertArgs( source_type, source_name, target_type, \
                    target_name, target_channels, target_rate )
        except Exception as e:
            return [ str(e), '' ]

        try:
            status = self.validateSourceType( source_type, source_name )
        except Exception as e:
            return [ str(e), '' ]

        try:
            self.convertType( source_type, source_name, target_type, \
                    target_name, target_channels, target_rate )
        except Exception as e:
            return [ str(e), '' ]

        return [ 'success', target_name ]


    def assertArgs(self, source_type, source_name, target_type, target_name, \
            target_channels, target_rate ):

        if not os.path.isfile( source_name ):
            raise Exception( "Error: file \'" + source_name + '\' not found' )
        if target_name == '':
            raise Exception( "Error: target filename not provided" )
        if target_type == '':
            raise Exception( "Error: target type not provided" )
        if target_rate < 0:
            raise Exception( "Error: target_rate can not be negative" )
        if target_channels < 0:
            raise Exception( "Error: target_channels can not be negative" )
        if target_channels > 8:
            raise Exception( "Error: target_channels can not be greater than 8" )

    def convertType(self, source_type, source_name, target_type, target_name, \
            target_channels, target_rate ):

        channels = ''
        rate = ''
        if target_type == 'flac':
            if target_channels != 0:
                channels = '--channels=' + str( target_channels )
            if target_rate != 0:
                rate = '--sample-rate=' + str( target_rate )

            command = 'flac -f ' + channels + ' ' + rate + " " + source_name + \
                ' -o ' + target_name + " --totally-silent --channel-map=none"
            flac_status = os.system( command )


            if os.path.isfile( target_name ) != True or flac_status != 0 :
                raise Exception( "Error: flac command malfunctioned. File path was"\
                        + source_name )
        else:
            if target_channels != 0:
                channels = '-c ' + str( target_channels )
            if target_rate != 0:
                rate = '-r ' + str( target_rate )
            command = "sox " + source_name + " " + channels + " " + rate + \
                    " " + target_name

            sox_status = os.system( command )

            if os.path.isfile( target_name ) != True or sox_status:
                raise Exception( "Error: SoX malfunctioned. File path was" + \
                        source_name )


    def validateSourceType( self, source_type, name ):

        [ source_file_name, source_extention ] = os.path.splitext( name )

        if source_type == 'nao_ogg':
            if source_extention != '.ogg':
                raise Exception( "Error: ogg type selected but file is of another type" )

        elif source_type == "nao_wav_1_ch" or source_type == 'headset':
            if source_extention != ".wav":
                raise Exception( "Error: wav type 1 channel selected but file is of another type" )

            samp_freq, signal = wavfile.read( name )
            if len( signal.shape ) != 1:
                error = ("Error: wav 1 ch declared but the audio file has " +\
                str(signal.shape[1]) + ' channels')
                raise Exception( error )

        elif source_type == "nao_wav_4_ch":
            if source_extention != ".wav":
                raise Exception( "Error: wav type 4 channels selected but file is of another type" )

            samp_freq, signal = wavfile.read( name )
            if len(signal.shape) != 2 or signal.shape[1] != 4:
                raise Exception( "Error: wav 4 ch declared but the audio file has not 4 channels" )

        else:
            raise Exception( "Non valid noise audio type" )
