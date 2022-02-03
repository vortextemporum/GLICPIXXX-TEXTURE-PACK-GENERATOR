import shutil
import os
import random

texturenames = ['red_stained_glass.png',
 'tnt_bottom.png',
 'red_sandstone.png',
 'sponge.png',
 'stripped_crimson_stem.png',
 'black_candle.png',
 'warped_wart_block.png',
 'cracked_deepslate_bricks.png',
 'sandstone.png',
 'warped_stem.png.mcmeta',
 'brewing_stand.png',
 'sweet_berry_bush_stage1.png',
 'powder_snow.png',
 'command_block_side.png',
 'bell_bottom.png',
 'white_candle_lit.png',
 'barrel_bottom.png',
 'azalea_plant.png',
 'jungle_trapdoor.png',
 'sand.png',
 'respawn_anchor_top.png',
 'dragon_egg.png',
 'potatoes_stage1.png',
 'furnace_front.png',
 'blue_candle.png',
 'chiseled_nether_bricks.png',
 'cake_bottom.png',
 'stripped_oak_log_top.png',
 'orange_stained_glass.png',
 'chorus_flower.png',
 'tinted_glass.png',
 'redstone_block.png',
 'repeating_command_block_conditional.png',
 'sweet_berry_bush_stage2.png',
 'stripped_oak_log.png',
 'command_block_front.png',
 'dirt_path_top.png',
 'honey_block_side.png',
 'smoker_side.png',
 'light_blue_candle_lit.png',
 'magenta_candle.png',
 'smoker_top.png',
 'chorus_flower_dead.png',
 'sculk_sensor_side.png',
 'observer_top.png',
 'observer_side.png',
 'poppy.png',
 'seagrass.png',
 'rose_bush_top.png',
 'tripwire_hook.png',
 'redstone_ore.png',
 'weathered_cut_copper.png',
 'command_block_back.png.mcmeta',
 'repeating_command_block_front.png.mcmeta',
 'repeating_command_block_side.png',
 'dead_brain_coral_fan.png',
 'twisting_vines.png',
 'stone_bricks.png',
 'lime_stained_glass_pane_top.png',
 'quartz_pillar.png',
 'dandelion.png',
 'dripstone_block.png',
 'water_still.png',
 'melon_side.png',
 'brown_concrete.png',
 'emerald_ore.png',
 'large_fern_bottom.png',
 'sandstone_top.png',
 'light_blue_terracotta.png',
 'command_block_conditional.png',
 'rose_bush_bottom.png',
 'dead_tube_coral.png',
 'oak_leaves.png',
 'birch_door_top.png',
 'iron_trapdoor.png',
 'white_wool.png',
 'carrots_stage0.png',
 'orange_glazed_terracotta.png',
 'cartography_table_top.png',
 'wither_rose.png',
 'lime_stained_glass.png',
 'destroy_stage_5.png',
 'mycelium_side.png',
 'wheat_stage7.png',
 'barrel_top.png',
 'nether_sprouts.png',
 'chain_command_block_front.png.mcmeta',
 'grindstone_side.png',
 'daylight_detector_inverted_top.png',
 'enchanting_table_side.png',
 'command_block_side.png.mcmeta',
 'chiseled_quartz_block.png',
 'pointed_dripstone_down_tip_merge.png',
 'potatoes_stage2.png',
 'crimson_trapdoor.png',
 'target_top.png',
 'light_blue_concrete_powder.png',
 'chiseled_polished_blackstone.png',
 'soul_campfire_log_lit.png',
 'jungle_door_top.png',
 'soul_fire_0.png.mcmeta',
 'black_shulker_box.png',
 'composter_ready.png',
 'polished_andesite.png',
 'smithing_table_top.png',
 'raw_copper_block.png',
 'bricks.png',
 'soul_campfire_fire.png.mcmeta',
 'campfire_fire.png.mcmeta',
 'bubble_coral_fan.png',
 'amethyst_cluster.png',
 'sunflower_front.png',
 'cauldron_inner.png',
 'campfire_fire.png',
 'magenta_candle_lit.png',
 'red_mushroom.png',
 'podzol_side.png',
 'peony_top.png',
 'white_candle.png',
 'pointed_dripstone_down_middle.png',
 'beetroots_stage1.png',
 'brown_glazed_terracotta.png',
 'lava_still.png.mcmeta',
 'yellow_shulker_box.png',
 'lectern_top.png',
 'dirt_path_side.png',
 'quartz_block_bottom.png',
 'mushroom_block_inside.png',
 'end_portal_frame_top.png',
 'stripped_jungle_log.png',
 'pink_shulker_box.png',
 'structure_block_corner.png',
 'wheat_stage4.png',
 'red_candle.png',
 'birch_sapling.png',
 'spruce_log.png',
 'debug.png',
 'yellow_concrete_powder.png',
 'green_candle_lit.png',
 'brain_coral.png',
 'cornflower.png',
 'red_concrete_powder.png',
 'red_tulip.png',
 'prismarine.png.mcmeta',
 'beetroots_stage3.png',
 'frosted_ice_3.png',
 'red_candle_lit.png',
 'rail.png',
 'gilded_blackstone.png',
 'chiseled_sandstone.png',
 'glass.png',
 'lectern_front.png',
 'purple_wool.png',
 'cake_top.png',
 'furnace_top.png',
 'tnt_side.png',
 'chain_command_block_side.png.mcmeta',
 'grass.png',
 'cracked_nether_bricks.png',
 'pink_concrete.png',
 'crimson_stem_top.png',
 'andesite.png',
 'deepslate_diamond_ore.png',
 'lily_of_the_valley.png',
 'dirt.png',
 'kelp.png',
 'nether_wart_stage2.png',
 'soul_campfire_log_lit.png.mcmeta',
 'dead_horn_coral.png',
 'horn_coral_fan.png',
 'orange_tulip.png',
 'orange_shulker_box.png',
 'destroy_stage_0.png',
 'clay.png',
 'orange_terracotta.png',
 'piston_inner.png',
 'kelp.png.mcmeta',
 'white_concrete_powder.png',
 'acacia_door_top.png',
 'rooted_dirt.png',
 'tube_coral_fan.png',
 'repeating_command_block_conditional.png.mcmeta',
 'lime_shulker_box.png',
 'nether_portal.png.mcmeta',
 'carrots_stage3.png',
 'purpur_pillar.png',
 'cobblestone.png',
 'birch_log_top.png',
 'lime_candle.png',
 'netherite_block.png',
 'cake_side.png',
 'cartography_table_side1.png',
 'dark_oak_trapdoor.png',
 'repeater_on.png',
 'chain_command_block_back.png',
 'cartography_table_side3.png',
 'tall_grass_bottom.png',
 'iron_door_top.png',
 'gray_concrete.png',
 'crafting_table_side.png',
 'smoker_bottom.png',
 'honeycomb_block.png',
 'light_blue_glazed_terracotta.png',
 'spruce_planks.png',
 'hopper_inside.png',
 'blue_orchid.png',
 'blast_furnace_front_on.png.mcmeta',
 'soul_torch.png',
 'lever.png',
 'respawn_anchor_top_off.png',
 'crimson_fungus.png',
 'bubble_coral.png',
 'gray_concrete_powder.png',
 'anvil.png',
 'black_candle_lit.png',
 'loom_top.png',
 'horn_coral.png',
 'light_gray_candle.png',
 'piston_top_sticky.png',
 'white_stained_glass_pane_top.png',
 'bamboo_stalk.png',
 'red_terracotta.png',
 'wheat_stage6.png',
 'item_frame.png',
 'small_dripleaf_top.png',
 'mossy_stone_bricks.png',
 'warped_stem.png',
 'tube_coral.png',
 'light_blue_wool.png',
 'destroy_stage_1.png',
 'pointed_dripstone_down_frustum.png',
 'oxidized_cut_copper.png',
 'lime_wool.png',
 'scaffolding_side.png',
 'smooth_stone_slab_side.png',
 'observer_back_on.png',
 'sculk_sensor_tendril_inactive.png.mcmeta',
 'smoker_front_on.png.mcmeta',
 'note_block.png',
 'black_stained_glass.png',
 'water_overlay.png',
 'dispenser_front_vertical.png',
 'potted_azalea_bush_side.png',
 'daylight_detector_top.png',
 'lantern.png',
 'composter_side.png',
 'bookshelf.png',
 'light_gray_glazed_terracotta.png',
 'white_concrete.png',
 'kelp_plant.png.mcmeta',
 'black_stained_glass_pane_top.png',
 'sugar_cane.png',
 'gray_stained_glass.png',
 'quartz_block_side.png',
 'light_blue_candle.png',
 'magenta_glazed_terracotta.png',
 'purple_glazed_terracotta.png',
 'red_shulker_box.png',
 'blast_furnace_front_on.png',
 'oak_door_bottom.png',
 'brain_coral_block.png',
 'chipped_anvil_top.png',
 'stripped_crimson_stem_top.png',
 'white_stained_glass.png',
 'lightning_rod.png',
 'dropper_front.png',
 'white_tulip.png',
 'respawn_anchor_side0.png',
 'dark_oak_sapling.png',
 'orange_concrete.png',
 'small_dripleaf_side.png',
 'destroy_stage_2.png',
 'oxeye_daisy.png',
 'command_block_conditional.png.mcmeta',
 'turtle_egg_slightly_cracked.png',
 'lightning_rod_on.png',
 'podzol_top.png',
 'blue_stained_glass.png',
 'fire_0.png',
 'chiseled_stone_bricks.png',
 'beehive_front_honey.png',
 'target_side.png',
 'redstone_lamp_on.png',
 'pointed_dripstone_up_frustum.png',
 'campfire_log.png',
 'cyan_stained_glass.png',
 'observer_back.png',
 'green_glazed_terracotta.png',
 'magenta_stained_glass.png',
 'nether_wart_stage0.png',
 'mushroom_stem.png',
 'blast_furnace_front.png',
 'diamond_block.png',
 'lime_concrete_powder.png',
 'smooth_stone.png',
 'soul_soil.png',
 'repeater.png',
 'comparator.png',
 'emerald_block.png',
 'yellow_wool.png',
 'honey_block_top.png',
 'dark_oak_log_top.png',
 'bamboo_small_leaves.png',
 'netherrack.png',
 'stripped_spruce_log.png',
 'cut_sandstone.png',
 'crying_obsidian.png',
 'crafting_table_front.png',
 'weeping_vines_plant.png',
 'bamboo_singleleaf.png',
 'pointed_dripstone_up_tip.png',
 'chiseled_quartz_block_top.png',
 'cauldron_bottom.png',
 'frosted_ice_0.png',
 'grass_block_side_overlay.png',
 'stonecutter_saw.png',
 'activator_rail.png',
 'stripped_warped_stem_top.png',
 'large_fern_top.png',
 'redstone_dust_line1.png',
 'end_stone_bricks.png',
 'large_amethyst_bud.png',
 'nether_gold_ore.png',
 'hopper_outside.png',
 'beetroots_stage0.png',
 'light_gray_stained_glass.png',
 'jigsaw_top.png',
 'pink_terracotta.png',
 'jungle_sapling.png',
 'stonecutter_top.png',
 'acacia_trapdoor.png',
 'copper_ore.png',
 'farmland_moist.png',
 'seagrass.png.mcmeta',
 'magenta_terracotta.png',
 'water_flow.png',
 'lectern_base.png',
 'purple_stained_glass.png',
 'purple_stained_glass_pane_top.png',
 'soul_fire_1.png.mcmeta',
 'observer_front.png',
 'moss_block.png',
 'soul_lantern.png',
 'small_dripleaf_stem_top.png',
 'structure_block.png',
 'iron_block.png',
 'glow_item_frame.png',
 'smooth_basalt.png',
 'fire_coral_fan.png',
 'destroy_stage_6.png',
 'beacon.png',
 'soul_lantern.png.mcmeta',
 'cyan_concrete_powder.png',
 'birch_door_bottom.png',
 'black_concrete.png',
 'loom_side.png',
 'repeating_command_block_back.png.mcmeta',
 'basalt_side.png',
 'purple_candle.png',
 'deepslate_iron_ore.png',
 'fire_1.png.mcmeta',
 'sculk_sensor_bottom.png',
 'deepslate_coal_ore.png',
 'polished_basalt_top.png',
 'bedrock.png',
 'oak_planks.png',
 'spawner.png',
 'torch.png',
 'grass_block_snow.png',
 'deepslate_tiles.png',
 'pink_tulip.png',
 'redstone_dust_line0.png',
 'grass_block_top.png',
 'pointed_dripstone_up_middle.png',
 'composter_top.png',
 'magenta_concrete.png',
 'blue_stained_glass_pane_top.png',
 'magma.png',
 'spruce_door_bottom.png',
 'nether_bricks.png',
 'spore_blossom_base.png',
 'command_block_back.png',
 'yellow_stained_glass_pane_top.png',
 'lime_candle_lit.png',
 'allium.png',
 'gray_wool.png',
 'sunflower_top.png',
 'budding_amethyst.png',
 'stripped_jungle_log_top.png',
 'grindstone_round.png',
 'gray_stained_glass_pane_top.png',
 'flowering_azalea_side.png',
 'light_blue_concrete.png',
 'bell_top.png',
 'pointed_dripstone_up_tip_merge.png',
 'crimson_planks.png',
 'shroomlight.png',
 'melon_top.png',
 'turtle_egg.png',
 'purpur_pillar_top.png',
 'cyan_stained_glass_pane_top.png',
 'repeating_command_block_side.png.mcmeta',
 'green_stained_glass.png',
 'fire_0.png.mcmeta',
 'potatoes_stage0.png',
 'repeating_command_block_back.png',
 'soul_fire_0.png',
 'small_amethyst_bud.png',
 'iron_ore.png',
 'cyan_candle_lit.png',
 'cracked_stone_bricks.png',
 'fletching_table_front.png',
 'birch_leaves.png',
 'crimson_roots_pot.png',
 'structure_block_save.png',
 'cyan_concrete.png',
 'brown_mushroom_block.png',
 'hay_block_top.png',
 'blue_terracotta.png',
 'prismarine.png',
 'respawn_anchor_side4.png',
 'grindstone_pivot.png',
 'brain_coral_fan.png',
 'pointed_dripstone_up_base.png',
 'stripped_birch_log_top.png',
 'yellow_glazed_terracotta.png',
 'light_gray_terracotta.png',
 'flowering_azalea_leaves.png',
 'end_rod.png',
 'magenta_wool.png',
 'dried_kelp_bottom.png',
 'glass_pane_top.png',
 'gray_shulker_box.png',
 'gray_glazed_terracotta.png',
 'quartz_pillar_top.png',
 'azalea_leaves.png',
 'deepslate_gold_ore.png',
 'rail_corner.png',
 'stripped_dark_oak_log.png',
 'chiseled_deepslate.png',
 'fletching_table_top.png',
 'cave_vines_lit.png',
 'flowering_azalea_top.png',
 'deepslate_emerald_ore.png',
 'raw_iron_block.png',
 'green_concrete_powder.png',
 'campfire_log_lit.png',
 'bee_nest_front.png',
 'chain_command_block_side.png',
 'pink_candle.png',
 'pumpkin_side.png',
 'dead_horn_coral_block.png',
 'chain_command_block_conditional.png',
 'bone_block_side.png',
 'green_terracotta.png',
 'lava_flow.png.mcmeta',
 'chain_command_block_front.png',
 'ice.png',
 'brown_terracotta.png',
 'blackstone.png',
 'cave_vines_plant.png',
 'daylight_detector_side.png',
 'pumpkin_top.png',
 'sandstone_bottom.png',
 'coal_ore.png',
 'cactus_top.png',
 'detector_rail_on.png',
 'dropper_front_vertical.png',
 'prismarine_bricks.png',
 'frosted_ice_1.png',
 'warped_roots.png',
 'dark_prismarine.png',
 'oak_sapling.png',
 'brown_mushroom.png',
 'black_concrete_powder.png',
 'cracked_polished_blackstone_bricks.png',
 'stone.png',
 'cut_copper.png',
 'potted_flowering_azalea_bush_top.png',
 'green_candle.png',
 'cobbled_deepslate.png',
 'bone_block_top.png',
 'carrots_stage1.png',
 'lapis_block.png',
 'brown_wool.png',
 'cake_inner.png',
 'lodestone_top.png',
 'dead_tube_coral_block.png',
 'composter_bottom.png',
 'cocoa_stage1.png',
 'warped_planks.png',
 'beehive_front.png',
 'gold_ore.png',
 'crafting_table_top.png',
 'beehive_end.png',
 'peony_bottom.png',
 'cauldron_top.png',
 'lava_flow.png',
 'light_gray_shulker_box.png',
 'fire_coral.png',
 'tall_seagrass_top.png',
 'dead_tube_coral_fan.png',
 'blue_glazed_terracotta.png',
 'honey_block_bottom.png',
 'cave_vines.png',
 'spruce_trapdoor.png',
 'warped_trapdoor.png',
 'sea_lantern.png.mcmeta',
 'dead_fire_coral.png',
 'dispenser_front.png',
 'end_portal_frame_side.png',
 'water_still.png.mcmeta',
 'smithing_table_front.png',
 'magenta_stained_glass_pane_top.png',
 'destroy_stage_7.png',
 'spruce_sapling.png',
 'blue_shulker_box.png',
 'deepslate_redstone_ore.png',
 'furnace_front_on.png',
 'green_concrete.png',
 'yellow_stained_glass.png',
 'horn_coral_block.png',
 'dead_bubble_coral_fan.png',
 'stripped_spruce_log_top.png',
 'weathered_copper.png',
 'brown_stained_glass_pane_top.png',
 'oak_log_top.png',
 'birch_planks.png',
 'anvil_top.png',
 'candle.png',
 'jukebox_top.png',
 'respawn_anchor_top.png.mcmeta',
 'activator_rail_on.png',
 'amethyst_block.png',
 'sculk_sensor_tendril_active.png.mcmeta',
 'stonecutter_saw.png.mcmeta',
 'twisting_vines_plant.png',
 'stripped_warped_stem.png',
 'pumpkin_stem.png',
 'warped_nylium_side.png',
 'potted_flowering_azalea_bush_side.png',
 'purple_terracotta.png',
 'respawn_anchor_bottom.png',
 'nether_wart_block.png',
 'light_gray_candle_lit.png',
 'acacia_leaves.png',
 'light_gray_wool.png',
 'repeating_command_block_front.png',
 'potted_azalea_bush_plant.png',
 'spore_blossom.png',
 'warped_fungus.png',
 'spruce_door_top.png',
 'deepslate_lapis_ore.png',
 'jungle_door_bottom.png',
 'yellow_candle.png',
 'fern.png',
 'spruce_leaves.png',
 'hanging_roots.png',
 'blue_wool.png',
 'diorite.png',
 'polished_deepslate.png',
 'damaged_anvil_top.png',
 'furnace_side.png',
 'green_wool.png',
 'red_glazed_terracotta.png',
 'black_wool.png',
 'tall_seagrass_bottom.png.mcmeta',
 'cyan_terracotta.png',
 'carrots_stage2.png',
 'campfire_log_lit.png.mcmeta',
 'orange_candle_lit.png',
 'attached_melon_stem.png',
 'bee_nest_side.png',
 'acacia_planks.png',
 'cartography_table_side2.png',
 'nether_portal.png',
 'blast_furnace_side.png',
 'crimson_door_bottom.png',
 'smoker_front_on.png',
 'stripped_dark_oak_log_top.png',
 'sea_lantern.png',
 'cave_vines_plant_lit.png',
 'vine.png',
 'light_gray_stained_glass_pane_top.png',
 'lectern_sides.png',
 'dried_kelp_side.png',
 'raw_gold_block.png',
 'blast_furnace_top.png',
 'birch_trapdoor.png',
 'cyan_glazed_terracotta.png',
 'redstone_dust_dot.png',
 'purple_candle_lit.png',
 'granite.png',
 'fire_coral_block.png',
 'detector_rail.png',
 'fletching_table_side.png',
 'big_dripleaf_side.png',
 'soul_campfire_fire.png',
 'crimson_door_top.png',
 'sculk_sensor_tendril_active.png',
 'brewing_stand_base.png',
 'dead_brain_coral_block.png',
 'red_sand.png',
 'bee_nest_front_honey.png',
 'brown_stained_glass.png',
 'tube_coral_block.png',
 'sweet_berry_bush_stage3.png',
 'jungle_log.png',
 'red_concrete.png',
 'polished_diorite.png',
 'warped_nylium.png',
 'green_stained_glass_pane_top.png',
 'glow_lichen.png',
 'tripwire.png',
 'wheat_stage3.png',
 'orange_stained_glass_pane_top.png',
 'red_wool.png',
 'beetroots_stage2.png',
 'respawn_anchor_side3.png',
 'powered_rail_on.png',
 'big_dripleaf_stem.png',
 'gold_block.png',
 'light_gray_concrete_powder.png',
 'oak_trapdoor.png',
 'stonecutter_side.png',
 'lime_concrete.png',
 'light_gray_concrete.png',
 'bell_side.png',
 'sea_pickle.png',
 'light_blue_stained_glass.png',
 'slime_block.png',
 'basalt_top.png',
 'brown_candle.png',
 'orange_wool.png',
 'cut_red_sandstone.png',
 'warped_roots_pot.png',
 'lantern.png.mcmeta',
 'jigsaw_lock.png',
 'jack_o_lantern.png',
 'warped_door_bottom.png',
 'destroy_stage_8.png',
 'tall_grass_top.png',
 'weeping_vines.png',
 'destroy_stage_9.png',
 'lily_pad.png',
 'light_blue_shulker_box.png',
 'jungle_leaves.png',
 'gray_candle.png',
 'dark_oak_planks.png',
 'exposed_cut_copper.png',
 'crimson_stem.png.mcmeta',
 'pink_stained_glass.png',
 'cracked_deepslate_tiles.png',
 'coal_block.png',
 'cocoa_stage0.png',
 'red_sandstone_top.png',
 'chain_command_block_back.png.mcmeta',
 'powered_rail.png',
 'yellow_candle_lit.png',
 'polished_basalt_side.png',
 'loom_front.png',
 'soul_fire_1.png',
 'acacia_log.png',
 'yellow_terracotta.png',
 'red_stained_glass_pane_top.png',
 'enchanting_table_top.png',
 'redstone_dust_overlay.png',
 'polished_granite.png',
 'purple_concrete.png',
 'tnt_top.png',
 'bubble_coral_block.png',
 'gray_candle_lit.png',
 'pink_candle_lit.png',
 'lilac_top.png',
 'green_shulker_box.png',
 'piston_bottom.png',
 'yellow_concrete.png',
 'pink_wool.png',
 'orange_candle.png',
 'end_stone.png',
 'bamboo_large_leaves.png',
 'snow.png',
 'stripped_birch_log.png',
 'potatoes_stage3.png',
 'quartz_bricks.png',
 'dark_oak_log.png',
 'frosted_ice_2.png',
 'redstone_torch_off.png',
 'scaffolding_top.png',
 'gray_terracotta.png',
 'smithing_table_side.png',
 'blue_candle_lit.png',
 'polished_blackstone_bricks.png',
 'dark_oak_door_top.png',
 'beehive_side.png',
 'coarse_dirt.png',
 'medium_amethyst_bud.png',
 'copper_block.png',
 'light_blue_stained_glass_pane_top.png',
 'nether_wart_stage1.png',
 'dead_brain_coral.png',
 'tall_seagrass_top.png.mcmeta',
 'acacia_door_bottom.png',
 'debug2.png',
 'piston_top.png',
 'azure_bluet.png',
 'terracotta.png',
 'barrel_side.png',
 'pink_concrete_powder.png',
 'dark_oak_door_bottom.png',
 'kelp_plant.png',
 'bee_nest_bottom.png',
 'lodestone_side.png',
 'deepslate_bricks.png',
 'azalea_top.png',
 'bamboo_stage0.png',
 'warped_stem_top.png',
 'polished_blackstone.png',
 'flower_pot.png',
 'cyan_shulker_box.png',
 'ancient_debris_side.png',
 'red_nether_bricks.png',
 'jukebox_side.png',
 'stripped_acacia_log.png',
 'sculk_sensor_top.png',
 'piston_side.png',
 'pointed_dripstone_down_base.png',
 'grass_block_side.png',
 'dead_bubble_coral_block.png',
 'bee_nest_top.png',
 'dead_bush.png',
 'magma.png.mcmeta',
 'smoker_front.png',
 'lapis_ore.png',
 'stripped_acacia_log_top.png',
 'iron_bars.png',
 'deepslate.png',
 'conduit.png',
 'white_terracotta.png',
 'enchanting_table_bottom.png',
 'purpur_block.png',
 'respawn_anchor_side2.png',
 'iron_door_bottom.png',
 'destroy_stage_4.png',
 'sweet_berry_bush_stage0.png',
 'wet_sponge.png',
 'composter_compost.png',
 'respawn_anchor_side1.png',
 'crimson_nylium.png',
 'lava_still.png',
 'magenta_concrete_powder.png',
 'dried_kelp_top.png',
 'fire_1.png',
 'brown_concrete_powder.png',
 'structure_block_data.png',
 'carved_pumpkin.png',
 'exposed_copper.png',
 'tuff.png',
 'crimson_nylium_side.png',
 'potted_flowering_azalea_bush_plant.png',
 'mycelium_top.png',
 'small_dripleaf_stem_bottom.png',
 'packed_ice.png',
 'acacia_sapling.png',
 'dead_horn_coral_fan.png',
 'sculk_sensor_tendril_inactive.png',
 'loom_bottom.png',
 'pink_stained_glass_pane_top.png',
 'ancient_debris_top.png',
 'blackstone_top.png',
 'soul_sand.png',
 'shulker_box.png',
 'red_mushroom_block.png',
 'lime_terracotta.png',
 'mossy_cobblestone.png',
 'birch_log.png',
 'farmland.png',
 'warped_door_top.png',
 'crimson_roots.png',
 'lime_glazed_terracotta.png',
 'chiseled_red_sandstone.png',
 'crimson_stem.png',
 'jigsaw_bottom.png',
 'dead_bubble_coral.png',
 'brown_candle_lit.png',
 'stonecutter_bottom.png',
 'tall_seagrass_bottom.png',
 'dead_fire_coral_fan.png',
 'lilac_bottom.png',
 'hopper_top.png',
 'candle_lit.png',
 'redstone_torch.png',
 'diamond_ore.png',
 'cauldron_side.png',
 'white_shulker_box.png',
 'wheat_stage0.png',
 'structure_block_load.png',
 'wheat_stage2.png',
 'sunflower_bottom.png',
 'dark_oak_leaves.png',
 'blue_concrete_powder.png',
 'deepslate_top.png',
 'chain_command_block_conditional.png.mcmeta',
 'red_sandstone_bottom.png',
 'dead_fire_coral_block.png',
 'magenta_shulker_box.png',
 'cobweb.png',
 'chorus_plant.png',
 'turtle_egg_very_cracked.png',
 'melon_stem.png',
 'obsidian.png',
 'big_dripleaf_tip.png',
 'wheat_stage5.png',
 'destroy_stage_3.png',
 'ladder.png',
 'scaffolding_bottom.png',
 'sunflower_back.png',
 'end_portal_frame_eye.png',
 'brown_shulker_box.png',
 'cactus_bottom.png',
 'cyan_candle.png',
 'calcite.png',
 'spruce_log_top.png',
 'jungle_planks.png',
 'pointed_dripstone_down_tip.png',
 'cactus_side.png',
 'hay_block_side.png',
 'oxidized_copper.png',
 'purple_concrete_powder.png',
 'orange_concrete_powder.png',
 'gravel.png',
 'pink_glazed_terracotta.png',
 'big_dripleaf_top.png',
 'purple_shulker_box.png',
 'deepslate_copper_ore.png',
 'smithing_table_bottom.png',
 'barrel_top_open.png',
 'blue_ice.png',
 'white_glazed_terracotta.png',
 'attached_pumpkin_stem.png',
 'oak_door_top.png',
 'wheat_stage1.png',
 'quartz_block_top.png',
 'azalea_side.png',
 'black_terracotta.png',
 'blue_concrete.png',
 'command_block_front.png.mcmeta',
 'jigsaw_side.png',
 'cyan_wool.png',
 'potted_azalea_bush_top.png',
 'comparator_on.png',
 'cocoa_stage2.png',
 'acacia_log_top.png',
 'water_flow.png.mcmeta',
 'nether_quartz_ore.png',
 'black_glazed_terracotta.png',
 'chain.png',
 'jungle_log_top.png',
 'redstone_lamp.png',
 'oak_log.png',
 'glowstone.png']

if not os.path.exists("./calmglicpixxx"):
    shutil.unpack_archive("./calmglicpixxx.zip")

allglicpix = os.listdir("calmglicpixxx")

if not os.path.exists("./temp"):
    os.makedirs("./temp/assets/minecraft/textures/block", exist_ok=True)
    shutil.copyfile("./pack.mcmeta", "./temp/pack.mcmeta")
    shutil.copyfile(os.path.join("./calmglicpixxx/",random.choice(allglicpix)), "./temp/pack.png")


for filename in texturenames:
    shutil.copyfile(os.path.join("./calmglicpixxx/",random.choice(allglicpix)), os.path.join("./temp/assets/minecraft/textures/block",filename))

shutil.make_archive("output", 'zip', "./temp")

    
shutil.rmtree("./temp")
shutil.rmtree("./calmglicpixxx")
