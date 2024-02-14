
/*
 * GPUPixel
 *
 * Created by gezhaoyou on 2021/6/24.
 * Copyright © 2021 PixPark. All rights reserved.
 */

#pragma once

#include "gpupixel_macros.h"

// base
#include "framebuffer.h"
#include "framebuffer_cache.h"
#include "gl_program.h"
#include "gpupixel_context.h"

// utils
#include "math_toolbox.h"
#include "util.h"

// source
#include "source.h"
#include "source_camera.h"
#include "source_image.h"
#include "source_raw_data_input.h"

// target
#include "target.h"
#include "target_raw_data_output.h"
#include "target_view.h"
#if defined(GPUPIXEL_IOS) || defined(GPUPIXEL_MAC)
#include "gpupixel_target.h"
#include "gpupixel_view.h"
#include "objc_target.h"
#endif

// base filters
#include "filter.h"
#include "filter_group.h"

// face filters
#include "beauty_face_filter.h"
#include "face_makeup_filter.h"
#include "face_reshape_filter.h"

#include "box_blur_filter.h"
#include "box_high_pass_filter.h"

// general filters
#include "bilateral_filter.h"
#include "brightness_filter.h"
#include "canny_edge_detection_filter.h"
#include "color_invert_filter.h"
#include "color_matrix_filter.h"
#include "contrast_filter.h"
#include "convolution3x3_filter.h"
#include "crosshatch_filter.h"
#include "directional_non_maximum_suppression_filter.h"
#include "directional_sobel_edge_detection_filter.h"
#include "emboss_filter.h"
#include "exposure_filter.h"
#include "gaussian_blur_filter.h"
#include "gaussian_blur_mono_filter.h"
#include "glass_sphere_filter.h"
#include "grayscale_filter.h"
#include "hsb_filter.h"
#include "halftone_filter.h"
#include "hue_filter.h"
#include "ios_blur_filter.h"
#include "luminance_range_filter.h"
#include "nearby_sampling3x3_filter.h"
#include "non_maximum_suppression_filter.h"
#include "pixellation_filter.h"
#include "posterize_filter.h"
#include "rgb_filter.h"
#include "saturation_filter.h"
#include "single_component_gaussian_blur_filter.h"
#include "single_component_gaussian_blur_mono_filter.h"
#include "sketch_filter.h"
#include "smooth_toon_filter.h"
#include "sobel_edge_detection_filter.h"
#include "sphere_refraction_filter.h"
#include "toon_filter.h"
#include "weak_pixel_inclusion_filter.h"
#include "white_balance_filter.h"


USING_NS_GPUPIXEL


#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

extern "C" {
    void* createSourceImage(const unsigned char* bytes, int width, int height) {
        // video data input
        std::shared_ptr<SourceRawDataInput> source_raw_input_;
        // beauty filter
        std::shared_ptr<BeautyFaceFilter> beauty_face_filter_;
        // video data output 
        std::shared_ptr<TargetRawDataOutput> target_raw_output_;
    
        stbi_write_jpg("input.jpg", width, height, 3, bytes, 1);

        gpupixel::GPUPixelContext::getInstance()->runSync([&] {
            // Create filter
            source_raw_input_ = SourceRawDataInput::create();
            target_raw_output_ = TargetRawDataOutput::create();
            // Face Beauty Filter
            beauty_face_filter_ = BeautyFaceFilter::create();
            
            // Add filter
            source_raw_input_->addTarget(beauty_face_filter_)
                            ->addTarget(target_raw_output_);

        });
            target_raw_output_->setPixelsCallbck([=](const uint8_t *data, 
                                                    int width, 
                                                    int height, 
                                                    int64_t ts) {
                stbi_write_png("result.png", width, height, 4, data, width * 4);
            });
            source_raw_input_->uploadBytes(bytes,
                                            width, 
                                            height, 
                                            width);
            // source_raw_input_->proceed();
    }
}
